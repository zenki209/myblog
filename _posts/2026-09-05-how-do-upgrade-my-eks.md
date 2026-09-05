---
layout: post
title: "How to Upgrade an EKS Cluster Without Downtime"
date: 2026-09-05
categories: [AWS, Kubernetes]
tags: [eks, kubernetes, aws, devops, platform-engineering]
---

Upgrading an Amazon EKS cluster safely is a controlled sequence of checks and
rolling changes. The goal is to remove deprecated APIs, upgrade the control
plane, replace worker nodes, update core add-ons, and verify application health
at each stage.

This checklist assumes that infrastructure changes are managed through
Terraform and application manifests are stored in GitOps repositories.

## Phase 1: Audit deprecated APIs

Before changing AWS resources, scan GitOps manifests and Helm charts for APIs
that are removed in the target Kubernetes version. For example,
`policy/v1beta1` PodDisruptionBudgets must be migrated to `policy/v1` before
the cluster is upgraded.

Use tools such as Pluto and Kubeconform in CI to find deprecated or invalid
resources. Give the upgrade a green light only after the manifests pass those
checks.

## Phase 2: Upgrade the control plane

The platform team triggers the control plane upgrade through Terraform. EKS
updates the managed control plane components, including the Kubernetes API
servers and `etcd`.

Kubernetes minor versions must be upgraded sequentially. For example, a
cluster cannot jump directly from 1.28 to 1.30; it must move from 1.28 to 1.29
and then from 1.29 to 1.30.

After the control plane upgrade completes, confirm that the API is available
and that the cluster reports the expected version before moving on to worker
nodes.

## Phase 3: Roll the worker nodes

Worker node replacement is where application downtime is most likely if the
workload is not configured for disruption. When the node group AMI is updated,
Kubernetes cordons and drains nodes one at a time.

Every highly available microservice should define a PodDisruptionBudget (PDB),
for example:

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
	name: example-service
spec:
	maxUnavailable: 1
	selector:
		matchLabels:
			app: example-service
```

Use either `minAvailable` or `maxUnavailable` to preserve the availability
level required by the service. Do not use both in the same PDB.

Also configure `topologySpreadConstraints` so replicas are distributed across
the cluster's Availability Zones. During a drain, Kubernetes will respect the
PDB and wait for replacement pods to become Ready before evicting protected
pods.

Before the rollout, verify that:

- Deployments have more than one available replica where required.
- Readiness probes accurately represent whether a pod can receive traffic.
- PDB selectors match the intended pods.
- New nodes are in service and have the expected labels and taints.

## Phase 4: Update core add-ons and verify observability

After the worker nodes are healthy, update the managed add-ons to versions
compatible with the new Kubernetes version. A common sequence is:

1. VPC CNI
2. CoreDNS
3. kube-proxy

The exact versions and order should follow the compatibility guidance for the
target EKS version. After each change, check pod health and cluster events.

Finally, verify live traffic in Grafana using the RED signals:

- **Rate:** Is traffic flowing at the expected volume?
- **Errors:** Did the error rate increase during the rollout?
- **Duration:** Did request latency change?

## Final checklist

- [ ] Deprecated APIs are removed or migrated.
- [ ] The control plane was upgraded one minor version at a time.
- [ ] PDBs, readiness probes, and replica counts protect availability.
- [ ] Worker nodes rolled over successfully.
- [ ] Managed add-ons are compatible with the target version.
- [ ] Grafana shows normal rate, error, and duration metrics.

An EKS upgrade is safest when each phase has an explicit validation step and
the rollout stops as soon as one of those checks fails.
---

Phase 1: Pre-Upgrade Deprecation Audit (Before touching AWS)
Kubernetes removes APIs between versions (e.g. policy/v1beta1 to policy/v1 for PodDisruptionBudgets).
• We scan our GitOps manifests and Helm charts using Pluto and Kubeconform in CI.
• Upgrade any deprecated API versions in code before the cluster version is bumped.
• Green light is given to the platform team only after all manifests pass.

---

Phase 2: Control Plane Upgrade (Managed by AWS)
The Central Cloud team triggers the control plane version bump via Terraform:
• EKS upgrades the managed control plane (API servers, etcd) with zero downtime.
• Rule: You cannot skip minor versions (e.g., 1.28 -> 1.30 is invalid; must go 1.28 -> 1.29 -> 1.30).

---

Phase 3: Worker Node Rolling Upgrade & Pod Disruption Budgets
This is where application downtime usually happens if misconfigured.
When the node group AMI is updated, Kubernetes cordons and drains nodes one by one.
To guarantee zero dropped requests:
• Every microservice must have a PodDisruptionBudget (PDB):
 minAvailable: 60% or maxUnavailable: 1
• topologySpreadConstraints ensure pods are spread evenly across 3 Availability Zones.
• As nodes drain, Kubernetes refuses to evict pods if it violates the PDB, waiting for new pods to be Ready on new nodes first.

---

Phase 4: Core Addon Updates & Observability Check
Once nodes are rolled over:
• Upgrade managed addons in sequence: VPC CNI -> CoreDNS -> kube-proxy.
• Verify live traffic in Grafana (RED metrics: Rate, Errors, Duration).
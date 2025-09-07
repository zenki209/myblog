---
layout: post
title: "GO: How to use Context in Go"
date: 2025-08-31
---
In Go, the `context` package is used to carry deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes. It is particularly useful in concurrent programming to manage the lifecycle of goroutines.

### Creating a Context

You can create a context using the `context.Background()` or `context.TODO()` functions. The former is used when you have a top-level context, while the latter is used when you're not sure which context to use.

```go
ctx := context.Background()
```

### Using Context with Goroutines

When spawning goroutines, it's essential to pass the context to ensure that they respect cancellation signals.

```go
go func(ctx context.Context) {
    // Do some work
}(ctx)
```

### Context with Timeout

You can create a context with a timeout using `context.WithTimeout()`. This is useful for operations that may take too long and need to be cancelled.

```go
ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
defer cancel()

select {
case <-time.After(3 * time.Second):
    fmt.Println("Operation completed")
case <-ctx.Done():
    fmt.Println("Operation cancelled:", ctx.Err())
}
```

### Conclusion

The `context` package is a powerful tool in Go for managing the lifecycle of requests and goroutines. By using contexts, you can ensure that your applications are more robust and can handle cancellations and timeouts gracefully.
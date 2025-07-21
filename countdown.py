def countdown(n):
    if n<=0:
        return 0
    else:
        print(f"countdown({n})->countdown(countdown({n-1}")
        return
        countdown(countdown(n-1))
print(countdown(3))



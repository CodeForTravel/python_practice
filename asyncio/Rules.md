# The Rules of Async IO

1. The `syntax` async def introduces either a `native coroutine` or an a`synchronous generator`. The expressions async with and async for are also valid, and you’ll see them later on.

2. The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”

## Rules for when and how you can and cannot use async/await.

1. Using await and/or return creates a coroutine function. To call a coroutine function, you must await it to get its results.

2. It is less common (and only recently legal in Python) to use yield in an async def block. This creates an asynchronous generator, which you iterate over with async for. Forget about async generators for the time being and focus on getting down the syntax for coroutine functions, which use await and/or return.

3. Anything defined with async def may not use yield from, which will raise a SyntaxError.


So on
# async_webdriver
Asynchronous selenium webdriver with safe threads

```ThreadPoolExecutor``` is used to parallelize tasks

```loop.run_in_executor``` allows make webdriver request asynchronously, but not threadsafe

```threading.lock.Lock``` instances acquires lock in each thread and realises when instruction is completed or exited, so it makes it threadsafe


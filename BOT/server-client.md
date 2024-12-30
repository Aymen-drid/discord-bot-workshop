```flowchart TD
    A[Bot Client] -->|1. Send Request| B[Discord API]
    B -->|2. Pending Promise| A
    A -->|3. Continue Other Tasks| C[Bot Processing]
    B -->|4. Return Response| D[Event Handler]
    D -->|5. Handle Success/Error| A  ```
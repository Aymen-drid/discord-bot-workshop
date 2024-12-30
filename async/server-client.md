```mermaid
sequenceDiagram
    participant A as Bot Client (client)
    participant B as Discord API (server)
    participant P as Promise

    A->>B: 1. Send Request
    B-->>A: 2. Response (Pending Promise)
    P->>A: 3. Success/Failure (Response Outcome)

  ```

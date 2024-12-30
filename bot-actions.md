## Discord Bot actions:
### Commands
- Trigger actions when users send messages with a specific prefix.
- Example: `!add` to check if the bot is online.
- Implemented using `commands.Bot()`.
### Events
- Capture actions like messages sent or users joining.
- Example: `on_message` to respond to user messages.
- Implemented with `discord.Client()` or `commands.Bot()`.
### Tasks (Background Tasks)
- Run tasks asynchronously in the background.
- Example: Periodic reminders or timed messages.
- Implemented with `discord.ext.tasks`.
### Permissions
- Control user access to certain commands or actions.
- Example: Only admins can use certain commands like `!ban`.
- Implemented with permission decorators (`@commands.has_permissions`).
### Intents
- Define which events the bot can access.
- Example: `discord.Intents.default()` enables basic events like `on_message`.
- Important for accessing sensitive data like user presence.
### Error Handling
- Catch and manage errors to ensure smooth bot operation.
- Example: Handle errors like `CommandNotFound` or permission issues.
- Implemented using `@bot.event` or `commands.CommandError`.

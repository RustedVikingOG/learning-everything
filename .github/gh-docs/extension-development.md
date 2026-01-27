# Building Chat Extensions

Guide to building VS Code extensions that extend GitHub Copilot chat.

## Extension Types

| Type | Purpose | API |
|------|---------|-----|
| Chat Participant | Custom @-mentionable assistant | `vscode.chat` |
| Language Model Tool | Tools for agent mode | `vscode.lm` |
| MCP Server Provider | Programmatic MCP registration | `vscode.lm.registerMcpServerDefinitionProvider` |

## Chat Participant

Create a custom assistant invoked with `@participant-name`:

### package.json

```json
{
  "contributes": {
    "chatParticipants": [
      {
        "id": "my-extension.code-reviewer",
        "name": "reviewer",
        "fullName": "Code Reviewer",
        "description": "Review code for issues",
        "isSticky": true,
        "commands": [
          {
            "name": "security",
            "description": "Focus on security issues"
          }
        ]
      }
    ]
  },
  "activationEvents": [
    "onChatParticipant:my-extension.code-reviewer"
  ]
}
```

### Handler Implementation

```typescript
import * as vscode from 'vscode';

const handler: vscode.ChatRequestHandler = async (
  request: vscode.ChatRequest,
  context: vscode.ChatContext,
  stream: vscode.ChatResponseStream,
  token: vscode.CancellationToken
) => {
  const prompt = request.command === 'security' 
    ? SECURITY_PROMPT 
    : BASE_PROMPT;

  const messages = [
    vscode.LanguageModelChatMessage.User(prompt),
    vscode.LanguageModelChatMessage.User(request.prompt)
  ];

  const response = await request.model.sendRequest(messages, {}, token);

  for await (const fragment of response.text) {
    stream.markdown(fragment);
  }
};

export function activate(context: vscode.ExtensionContext) {
  const participant = vscode.chat.createChatParticipant(
    'my-extension.code-reviewer',
    handler
  );
  participant.iconPath = vscode.Uri.joinPath(
    context.extensionUri, 
    'icon.png'
  );
}
```

## Response Stream Methods

```typescript
stream.markdown('**Bold** text');           // Markdown content
stream.progress('Analyzing...');            // Progress message
stream.reference(uri);                      // File reference
stream.anchor(uri, 'Link text');           // Clickable link
stream.button({ title: 'Run', command: 'ext.run' }); // Action button
```

## Language Model API

Direct access to AI models:

```typescript
const [model] = await vscode.lm.selectChatModels({
  vendor: 'copilot',
  family: 'gpt-4o'
});

const messages = [
  vscode.LanguageModelChatMessage.User('Explain this code')
];

const response = await model.sendRequest(messages, {}, token);

for await (const chunk of response.text) {
  console.log(chunk);
}
```

## MCP Server Provider

Register MCP servers programmatically:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.lm.registerMcpServerDefinitionProvider('myProvider', {
      provideMcpServerDefinitions: async () => [
        new vscode.McpStdioServerDefinition({
          label: 'myServer',
          command: 'node',
          args: ['server.js'],
          cwd: vscode.Uri.file('/path/to/server')
        })
      ]
    })
  );
}
```

## Resources

- [Chat Extension Tutorial](https://code.visualstudio.com/api/extension-guides/ai/chat-tutorial)
- [Language Model API Guide](https://code.visualstudio.com/api/extension-guides/ai/language-model)
- [Chat Sample Extension](https://github.com/microsoft/vscode-extension-samples/tree/main/chat-sample)

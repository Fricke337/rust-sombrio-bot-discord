# Rust Sombrio - Bot Discord 🛡️

Sistema de automação profissional desenvolvido em Python para a gestão do servidor de Rust "Sombrio [BR/LATAM]". Este projeto foca em escalabilidade de atendimento e organização de comunidade.

## 🧠 Lógica de Persistência de Componentes
Um dos diferenciais deste projeto é a implementação de **Persistent Views**. Ao contrário de bots simples, onde os botões param de funcionar após um restart do script, este bot utiliza `custom_id` vinculados à classe `TicketView`. Isso garante que, mesmo que o bot sofra uma queda ou manutenção, os botões de "Abrir Chamado" postados anteriormente continuem operacionais assim que o sistema retornar ao estado `online`.

## ✨ Funcionalidades
- **Triagem de Atendimento:** Canais distintos para Suporte/VIP e Denúncias, otimizando o tempo de resposta da staff.
- **Automação de Permissões:** Criação de canais privados on-the-fly com `PermissionOverwrite` restrito ao autor do chamado.
- **Interface Visual:** Utilização de Rich Embeds para uma comunicação clara e profissional das diretrizes do servidor.

## 🛠️ Stack Tecnológica
- Python 3.14
- Discord.py (Advanced UI Components)
- Asynchronous Programming
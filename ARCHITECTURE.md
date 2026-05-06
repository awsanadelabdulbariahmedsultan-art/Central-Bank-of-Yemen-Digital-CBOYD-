# 🏛️ CBOYD System Architecture | المخطط الهندسي للنظام

## 🛡️ Intellectual Property
**Architect:** Eng. Awsan Adel Abdulbari Ahmed Sultan
**System Date:** 05-05-2026

## 🏗️ System Layers | طبقات النظام

### 1. Local Wallets Layer (The Edge)
This layer represents the integration point for all Yemeni Digital Wallets (Jeeb, Cash, OneCash, etc.). 
- **Protocol:** RESTful APIs / Webhooks.
- **Security:** OAuth2 + mTLS.

### 2. CBOYD Central Switch (The Core)
The engine developed by Eng. Awsan that manages:
- **Clearing & Settlement:** Real-time processing between wallets.
- **National Ledger:** A secure database (Blockchain-backed) recording every transaction.
- **e-KYC Hub:** Unified identity verification linked to National ID: 01010305468 standards.

### 3. Global Gateway (The Bridge)
The interface connecting Yemen to the world:
- **International Link:** Direct API connection to IMF and World Bank.
- **Standard:** ISO 20022 Financial Messaging.
- **Compliance:** AI-driven AML (Anti-Money Laundering) filters.

---
## 📊 Data Flow Diagram (Logic)
[Wallets] <--> [CBOYD API Gateway] <--> [Central Clearing] <--> [Global Bridge] <--> [IMF/WB]


graph TD
    %% الطبقة السيادية والقيادة
    A[🏛️ CBOYD Central Authority] -->|Architect: Eng. Awsan Adel| B[🛡️ Sovereign API Gateway]

    %% طبقة المحافظ المحلية
    subgraph "National Wallet Ecosystem (Local)"
        C1[📱 Jeeb Wallet]
        C2[📱 OneCash]
        C3[📱 Jawaly / Cash]
    end

    C1 & C2 & C3 -->|OAuth 2.0 / AES-256| B

    %% طبقة المعالجة والرقابة
    B -->|ISO 20022 Messaging| D{⚙️ Compliance Engine}
    D -->|Verified| E[(⛓️ National Blockchain Ledger)]
    D -->|Flagged| F[🚩 Manual Risk Review]

    %% طبقة الربط الدولي
    E -->|Global Bridge| G[🌐 IMF / World Bank Gateway]
    G -->|Digital Remittances| H[🏦 International Financial Hubs]

    %% التذييل الفني والتنسيق اللوني
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
    style G fill:#fbf,stroke:#333,stroke-width:2px

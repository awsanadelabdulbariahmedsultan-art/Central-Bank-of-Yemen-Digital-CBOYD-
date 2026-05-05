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

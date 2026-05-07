# 🚀 CBOYD API Documentation v1.0 | توثيق بروتوكول الربط الرقمي

## 🛡️ Identity & Authorization | الهوية والتفويض
**Lead Architect & Founder:** Eng. Awsan Adel Abdulbari Ahmed Sultan
**National ID:** 01010305468 | **Release Date:** 05-05-2026

To integrate with the **Central Bank of Yemen Digital (CBOYD)**, all Payment Service Providers (PSPs) like Jaib, Cash, Onecash, Floosak, Shilling, Aden Cash, Mahfathati, Amfloos (Kurimi), Jawaly, Mobile Money and others must use **OAuth 2.0** with a Central Private Key issued by Eng. Awsan Adel Abdulbari Ahmed Sultan.

---

## 📍 Inbound Endpoints (Local Wallets to CBOYD) | بوابات الربط المحلية

### 1. Register Wallet Node | تسجيل محفظة جديدة
`POST /api/v1/node/register`
- **Purpose:** Linking the local wallet server to the CBOYD central infrastructure.
- **Payload:** `{ "wallet_id": "string", "provider": "string", "timestamp": "ISO8601" }`

### 2. Real-Time Transaction Settlement | تسوية العمليات لحظياً
`POST /api/v1/settle`
- **Purpose:** Moving funds between different local wallets (e.g., Cash to Jawaly) via CBOYD switch.
- **Security:** Requires Sovereign Bearer Token.

---

## 🌐 Outbound Endpoints (CBOYD to Global Bridge) | بوابات الربط الدولية

### 1. IMF/World Bank Data Sync | الربط مع صندوق النقد والبنك الدولي
`POST /api/v1/global/sync`
- **Standard:** Compliant with **ISO 20022** Financial XML format.
- **Description:** Direct secure data transmission to international financial hubs.

### 2. Cross-Border Remittance Bridge | جسر الحوالات الدولية
`POST /api/v1/bridge/transfer`
- **Purpose:** Enabling international aid and trade payments directly into local digital wallets.

---

## 🔍 Transaction Verification | التحقق من العمليات
`GET /api/v1/verify/{tx_id}`
- **Purpose:** Real-time audit of any transaction on the national blockchain ledger.

---

## ⚠️ Compliance & Security | الامتثال والأمان
- **e-KYC:** Mandatory identity matching with the CBOYD Unified Identity protocol.
- **AML Check:** AI-driven Anti-Money Laundering scanning on every transaction.
- **Encryption:** AES-256 bit encryption for all data at rest and in transit.

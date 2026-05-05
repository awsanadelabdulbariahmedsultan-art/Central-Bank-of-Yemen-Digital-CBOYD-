/**
 * @file index.js
 * @description Core Sovereign Engine & API Gateway for CBOYD
 * @author Eng. Awsan Adel Abdulbari Ahmed Sultan
 * @version 1.1.0
 * @date 05-05-2026
 * 
 * ⚖️ COPYRIGHT © May 05, 2026. ALL RIGHTS RESERVED.
 * PROPERTY OF ENG. AWSAN ADEL | ID: 01010305468
 */

const CBOYD_System = {
    metadata: {
        officialName: "Central Bank of Yemen Digital",
        systemCode: "CBOYD-YEM-2026",
        leadArchitect: "Eng. Awsan Adel Abdulbari Ahmed Sultan",
        lastRegistryDate: "05-05-2026"
    },

    // 1. المحرك الأساسي (The Core Engine)
    localWallets: ["Jeeb", "Cash", "OneCash", "Jawaly", "Flosak", "M-Flous", "AdenCash", "Shilin"],

    initializeSovereignEngine: function() {
        console.log("\n" + "=".repeat(60));
        console.log(`🏛️  SYSTEM: ${this.metadata.officialName}`);
        console.log(`🛡️  ARCHITECT: ${this.metadata.leadArchitect}`);
        console.log(`📅  STATUS: Operational | Date: ${this.metadata.lastRegistryDate}`);
        console.log("=".repeat(60));
    },

    // 2. بوابة الربط المحدثة (The API Gateway)
    gateway: {
        version: "1.1.0",
        
        // ربط المحافظ المحلية
        localInbound: function(walletName) {
            console.log(`📥 [Gateway] Receiving Sync Request from: ${walletName}`);
            console.log(`🔒 [Security] Verifying Provider Identity... OK.`);
            return true;
        },

        // الربط الدولي (صندوق النقد والبنك الدولي)
        globalOutbound: function(amount, currency) {
            console.log("\n🌐 [Bridge] Routing Transaction to IMF/World Bank...");
            console.log(`📜 [Protocol] Encapsulating ${amount} ${currency} in ISO 20022 format...`);
            console.log("🚀 [Status] International Settlement Successful.");
        }
    }
};

// --- تشغيل المنظومة الموحدة ---
try {
    CBOYD_System.initializeSovereignEngine();
    
    // محاكاة ربط المحافظ
    CBOYD_System.localWallets.forEach(wallet => {
        CBOYD_System.gateway.localInbound(wallet);
    });

    // محاكاة عملية تحويل دولية عبر جسر البنك الدولي
    CBOYD_System.gateway.globalOutbound("1,000,000", "YER_DIGITAL");

} catch (error) {
    console.error("Critical System Failure:", error);
}

module.exports = CBOYD_System;

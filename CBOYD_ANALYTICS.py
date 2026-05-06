"""
🏛️ PROJECT: Central Bank of Yemen Digital (CBOYD)
🛡️ MODULE: Predictive Analytics & Stability Core
⚖️ COPYRIGHT © 2026 | ALL RIGHTS RESERVED
---------------------------------------------------------
AUTHOR: Eng. Awsan Adel Abdulbari Ahmed Sultan
ID: 01010305468 | YEMEN
LINKEDIN: https://www.linkedin.com/in/awsan-adel-abdulbari-ahmed-sultan-8aa5a1a9?utm_source=share_via&utm_content=profile&utm_medium=member
---------------------------------------------------------
DESCRIPTION:
This engine simulates the impact of digital adoption on Yemen's 
systemic stability and predicts financial crisis probabilities.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class CBOYD_Analytics_Core:
    def __init__(self, periods=120):
        self.T = periods
        self.architect = "Eng. Awsan Adel"
        np.random.seed(42)
        
        # مؤشرات الأداء الرئيسية (KPIs) لـ CBOYD
        self.digital_adoption = np.zeros(self.T)
        self.liquidity_stability = np.zeros(self.T)
        self.crisis_probability = np.zeros(self.T)
        self.exchange_rate_stability = np.zeros(self.T)
        self.ssi = np.zeros(self.T) # Systemic Stability Index

    def run_simulation(self):
        self.digital_adoption[0] = 0.1
        self.liquidity_stability[0] = 0.8
        self.exchange_rate_stability[0] = 0.7
        
        for t in range(1, self.T):
            # محاكاة ذكية للنمو الرقمي تحت إشراف المهندس أوسان
            shock = np.random.normal(0, 0.01)
            self.digital_adoption[t] = np.clip(self.digital_adoption[t-1] + 0.005 + (0.1 * shock), 0, 1)

            # تحسن الاستقرار مع زيادة الرقمنة (منطق CBOYD)
            self.exchange_rate_stability[t] = np.clip(self.exchange_rate_stability[t-1] + (0.02 * self.digital_adoption[t]) + shock, 0, 1)
            self.liquidity_stability[t] = np.clip(self.liquidity_stability[t-1] - (0.01 * (1 - self.digital_adoption[t])) + abs(shock), 0, 1)
            
            # حساب مؤشر الاستقرار النظامي (الخوارزمية السيادية)
            self.ssi[t] = (0.4 * self.digital_adoption[t] + 0.4 * self.exchange_rate_stability[t]) - (0.2 * (1-self.liquidity_stability[t]))
            
            # منطق التنبؤ بالأزمات (Predictive Risk Logic)
            z = - (4 * self.ssi[t] - 2)
            self.crisis_probability[t] = 1 / (1 + np.exp(z))

        return self.generate_visual_report()

    def generate_visual_report(self):
        plt.style.use('dark_background') # تنسيق عصري واحترافي
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # الرسم الأول: التحول الرقمي والاستقرار
        ax1.plot(self.digital_adoption, label='CBOYD Digital Adoption', color='#2ecc71', lw=3)
        ax1.plot(self.ssi, label='Systemic Stability Index (SSI)', color='#3498db', lw=2, linestyle='--')
        ax1.set_title(f'CBOYD: Stability Projection - Architect: {self.architect}', fontsize=14, color='white')
        ax1.set_ylabel('Index Value')
        ax1.legend()
        ax1.grid(alpha=0.2)

        # الرسم الثاني: احتمالية الأزمة
        ax2.fill_between(range(self.T), self.crisis_probability, color='#e74c3c', alpha=0.2)
        ax2.plot(self.crisis_probability, color='#e74c3c', lw=2, label='Crisis Probability %')
        ax2.axhline(0.7, color='yellow', linestyle=':', label='Alert Level')
        ax2.set_title('Risk Prediction Model (AI-Based)', fontsize=14, color='white')
        ax2.set_xlabel('Timeline (Months)')
        ax2.legend()
        ax2.grid(alpha=0.2)

        plt.tight_layout()
        plt.savefig('CBOYD_Analytics_Report.png') # حفظ الرسم تلقائياً للعرض
        plt.show()
        
        return pd.DataFrame({
            'Month': range(self.T),
            'Adoption': self.digital_adoption,
            'Stability': self.ssi,
            'Risk_Prob': self.crisis_probability
        })

# تشغيل المحرك التنبؤي
if __name__ == "__main__":
    engine = CBOYD_Analytics_Core()
    report = engine.run_simulation()
    print(f"--- CBOYD Analytics Core v1.0 | Registered to: {engine.architect} ---")
    print(report.tail())

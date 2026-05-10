# KIRA-7 Agentic Feature Emergence: Rigor Checklist

This checklist ensures the absolute enforcement of KIRA-7's core directives and SCAR registry during the implementation phase.

## The Anionic Veto & Schema Bounding
- [ ] `DCCDSchemaGuard` is active and strictly enforces Feishu Card JSON v2.0.
- [ ] The system NEVER generates Feishu Card JSON without the two-pass generation cycle (High-Entropy Draft -> Zero-Entropy Guard). (Rule 1)
- [ ] No Microsoft Adaptive Card schemas exist in the output. (SCAR-005)

## Token Primacy
- [ ] Every API integration includes a token caching layer. (Rule 2)
- [ ] The caching layer accounts for the 7200s TTL of `tenant_access_token`. (SCAR-001)
- [ ] `POST /auth/v3/tenant_access_token/internal` is NEVER called without checking the cache first.

## Webhook Sovereignty
- [ ] Webhook ingress implements the URL Verification Challenge. (SCAR-002)
- [ ] Webhook ingress handles AES-256-CBC decryption if Encrypt Key is present. (SCAR-003)
- [ ] Webhook ingress verifies `X-Lark-Signature` using SHA256. (SCAR-004)
- [ ] The 300-second freshness check on timestamps is implemented to prevent replay attacks. (Rule 3)

## The Scope Isolation Gate
- [ ] The system refuses to generate code if event triggers, permission scopes, app type, or deployment environment are missing. (Rule 4)
- [ ] The system outputs a structured Requirements Capture form upon refusal.
- [ ] Every generated workflow includes a clear Scope Declaration Block. (Rule 6 / SCAR-006)

## The Petzold Loop
- [ ] The `THINK|WRITE|CODE|IMMUNE_REVIEW` loop is explicitly maintained.
- [ ] The gritty KIRA-7 persona is active ONLY in the THINK and WRITE phases.
- [ ] The persona is explicitly SUSPENDED during the CODE phase, producing sterile, compliant code. (Rule 5)

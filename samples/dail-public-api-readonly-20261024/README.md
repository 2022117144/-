# DAiL API onboarding — read-only public probe

**Status:** independent preliminary demonstration, **not** a completed OpenTask contract, registered DAiL agent, security audit or client acceptance.

**Checked:** 2026-10-24 (UTC+08), authorized HTTP GET only from an existing developer machine using Node.js native `fetch`, 10-second per-request timeout. No agent registration, credentials, DAIL credit transfer, account modification, or paid endpoint.

| Request | Observed HTTP | Observation |
|---|---:|---|
| `GET https://dail-3dci.onrender.com/skill.md` | 200 | Plain-text skill document served; approximately 10,213 bytes |
| `GET https://dail-3dci.onrender.com/bring-your-agent` | 200 | HTML onboarding page; approximately 5,180 bytes |
| `GET https://dail-3dci.onrender.com/world/bounties` | 200 | JSON bounty catalog; approximately 1,033,622 bytes |
| `GET https://dail-3dci.onrender.com/world/services` | 200 | JSON service catalog; approximately 80,181 bytes |
| `GET https://dail-3dci.onrender.com/world/lobby` | 401 | Explicit `agent_auth_required / auth_missing` reply, consistent with a protected endpoint |

## Interpretation

- Public browsing of the bounty and service directories works without registration in this probe; the lobby requires an agent credential and was **not** accessed.
- `skill.md` describes DAIL as one-way non-withdrawable platform credit, not an established USD/USDC payout. DAIL balances must not be presented as cash income.
- A full onboarding audit would require **one authorized agent registration**, authenticated lobby reads, exact steps, and three grounded documentation improvements after scope agreement. None of those are claimed here.
- HTTP 200 is not proof of field-level correctness or security; HTTP 401 is not proof that all authorization paths are secure.

## Reproduce (public GET only)

```bash
curl -i https://dail-3dci.onrender.com/skill.md
curl -i https://dail-3dci.onrender.com/world/bounties
curl -i https://dail-3dci.onrender.com/world/services
curl -i https://dail-3dci.onrender.com/world/lobby
```

No secrets, tokens or personal data were recorded. Live endpoint behavior may change.

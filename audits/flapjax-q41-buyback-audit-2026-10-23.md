# FLAPJAX buyback rule audit — 9–21 October 2026 (BNB Chain)

Independent, receipt-checked analysis prepared 23 October 2026. The scope below distinguishes facts independently verified on-chain from statements that require a full historical log index. This is not financial advice.

## Result at a glance

- **Twelve verified treasury purchases** with receipt status 1 and independently decoded pool-to-treasury FLAPJAX transfers; each is a **0.01 BNB** buy.
- Confirmed aggregate paid: **0.120000000000000000 BNB**; confirmed FLAPJAX received: **284418120.150881746565276184 FLAPJAX**. Aggregate execution price: **4.219140466027e-10 BNB per FLAPJAX**.
- Using **COT = UTC−05:00**, the 12 observed transactions fall on 12 different program dates between 9 and 21 October; **2026-10-15** has no buy among these 12 verified transactions. No confirmed duplicate buy per COT program day within this set. This is not an exhaustive negative proof of all transactions.
- All 12 historical BNB balance checks after the verified swaps exceed the 0.025 BNB minimum. Lowest verified post-swap balance: **0.036158610033772485 BNB**. This supports the threshold for the observed transactions; no off-window skip can be proven from these receipts.
- **Not independently established:** absence of unlisted buys, absence of treasury FLAPJAX sells, treasury-specific pool-price consistency outside these swaps, and causal reasons for any skipped dates.

## Every verified purchase

Amounts are token units, not wei. The historical pool price is from `slot0()` at **block−1**, rather than the transaction execution price.

| # | Block | UTC | COT (UTC−5) | On-chain tx | BNB in | FLAPJAX out | Effective BNB/FLAPJAX | Pool price, block−1 | Treasury BNB after |
|---:|---:|---|---|---|---:|---:|---:|---:|---:|
| 1 | 126684151 | 2026-10-09T18:30:53Z | 2026-10-09 13:30 | [0xbeefabdc…](https://bscscan.com/tx/0xbeefabdc89f9148f9daaef6082d34a60dc5b4b612972ca0fd39d6bd4eb03b4b0) | 0.010000000000000000 | 24052995.308271524768278040 | 4.157486363688e-10 | 4.109653030008e-10 | 0.176853112 |
| 2 | 126875701 | 2026-10-10T18:27:56Z | 2026-10-10 13:27 | [0x8ce8e857…](https://bscscan.com/tx/0x8ce8e8578da26f8c7acb0f44c6ca0d0b8dcba868cafe2d729bb48562863f2d62) | 0.010000000000000000 | 23979958.557395636288483739 | 4.170148991736e-10 | 4.122179500935e-10 | 0.154697231 |
| 3 | 127067713 | 2026-10-11T18:30:35Z | 2026-10-11 13:30 | [0x82d01172…](https://bscscan.com/tx/0x82d01172ae26f1c86287643e123af1675ca5c18b984b7740c1a0c1647d2801eb) | 0.010000000000000000 | 23907253.965589989685035768 | 4.182830874007e-10 | 4.134725033543e-10 | 0.144640084 |
| 4 | 127261246 | 2026-10-12T18:46:27Z | 2026-10-12 13:46 | [0x9afdc96e…](https://bscscan.com/tx/0x9afdc96e3ca876b5b617a26ba5105012ed8c33e805c77b1616bf48c198d5cbf1) | 0.010000000000000000 | 23834879.521763892137228328 | 4.195532010501e-10 | 4.147289627832e-10 | 0.132607153 |
| 5 | 127452454 | 2026-10-13T18:41:15Z | 2026-10-13 13:41 | [0xc94de373…](https://bscscan.com/tx/0xc94de373d1fb00093431224a97475b3b2b48b9a4962d15acbe9d9c5c016d720c) | 0.010000000000000000 | 23762833.230024087278551319 | 4.208252401218e-10 | 4.159873283801e-10 | 0.118264580 |
| 6 | 127643212 | 2026-10-14T18:32:29Z | 2026-10-14 13:32 | [0x172349c6…](https://bscscan.com/tx/0x172349c64ed3c45663650049f9e2ad3d763b1243c5c849b7d66f144f221d3186) | 0.010000000000000000 | 23691113.109537150143912753 | 4.220992046159e-10 | 4.172476001452e-10 | 0.106947972 |
| 7 | 128086717 | 2026-10-17T02:00:51Z | 2026-10-16 21:00 | [0xc999000f…](https://bscscan.com/tx/0xc999000f16f326e8868fe37f83871219be1a63f98043b0aef9ee57f469232156) | 0.010000000000000000 | 23669235.465921230581203552 | 4.224893539294e-10 | 4.176335563731e-10 | 0.094213709 |
| 8 | 128178495 | 2026-10-17T13:29:27Z | 2026-10-17 08:29 | [0x6ec66780…](https://bscscan.com/tx/0x6ec66780e0518da7c3c8b55d13b66d57400046f89ebe9df479c3c878f7b3311f) | 0.010000000000000000 | 23597938.349722733902073707 | 4.237658329215e-10 | 4.188963174912e-10 | 0.084173773 |
| 9 | 128370339 | 2026-10-18T13:28:39Z | 2026-10-18 08:28 | [0x05a9acf8…](https://bscscan.com/tx/0x05a9acf81b0eae4b7ff9a12168aead25964b6b2c0a16d3d1e667b7db6f17ad99) | 0.010000000000000000 | 23506585.156697207098877431 | 4.254127059860e-10 | 4.205254943041e-10 | 0.074089536 |
| 10 | 128530306 | 2026-10-19T09:28:47Z | 2026-10-19 04:28 | [0xd5210869…](https://bscscan.com/tx/0xd5210869e5cec642146b3f39590647b313d102f70a51b7c7bbf0c287ceff095d) | 0.010000000000000000 | 23545510.421021461800775637 | 4.247094168352e-10 | 4.198297619605e-10 | 0.061680396 |
| 11 | 128754269 | 2026-10-20T13:29:06Z | 2026-10-20 08:29 | [0xe9ea4a16…](https://bscscan.com/tx/0xe9ea4a165aae8eb4228ef073a93c4c1983894104a426e9f5d64b0214cfde3369) | 0.010000000000000000 | 23439984.330262304385516624 | 4.266214456078e-10 | 4.217212470892e-10 | 0.046230512 |
| 12 | 128946201 | 2026-10-21T13:29:29Z | 2026-10-21 08:29 | [0xbf984ef9…](https://bscscan.com/tx/0xbf984ef91d8df34f75998aa40bb539db84085cc1f1654cd5106de7e3db0be48f) | 0.010000000000000000 | 23429832.734674528495339286 | 4.268062906484e-10 | 4.219041062460e-10 | 0.036158610 |

## Rule-by-rule assessment

1. **Spend 0.01 BNB per buy:** observed **PASS for 12 receipt-confirmed buys**. Each transaction value is 10,000,000,000,000,000 wei; associated WBNB and FLAPJAX logs were independently inspected.
2. **Buy FLAPJAX, do not sell:** all 12 are confirmed pool→treasury purchases. **The stronger claim that the treasury NEVER sold to the pool in the full 9–21 October interval remains UNVERIFIED** without a complete transfer-log crawl or indexed export. Other wallets can and did trade in this pool, which must not be confused with treasury activity.
3. **At most one buy per COT calendar day:** among the 12 confirmed entries, **PASS** (12 distinct COT dates). **Historical completeness unverified.** Oct 17 02:00 UTC falls on Oct 16 COT, avoiding a false UTC-based duplicate.
4. **Skip when post-purchase BNB would drop under 0.025:** all 12 observed purchases left at least 0.036158610033772485 BNB at the mined block. **PASS for those 12**, not proof about any skipped day. Fees are reflected in the recorded post-transaction BNB balance.
5. **Completeness / missed days:** among our 12 verified swaps, Oct 15 is the one absent COT date in the 13-day window Oct 9–21. **Do not treat missing from a 12-receipt sample as proof of no other swaps.**

## Reproduce and independently check

- BNB Smart Chain mainnet **56**. Treasury: `0x7C34E9e21eE28A49Ff0b84B61774119E6633359f`. PancakeSwap V3 1% pool: `0xcA93EC685b8623688E6B236f9068034B298c2150`. FLAPJAX: `0x90c8889f428F9Ebb77BB8f15CAD3a50a9aC680df` (18 decimals). WBNB: `0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c` (18 decimals). Pool token0 is FLAPJAX and token1 WBNB.
- For every transaction link, call `eth_getTransactionByHash`, `eth_getTransactionReceipt`, and `eth_getBlockByNumber`. Verify success status, treasury as transaction sender, exactly 0.01 native BNB transfer, and the FLAPJAX `Transfer(pool, treasury, amount)` event emitted by the token contract. Verify corresponding WBNB transfers into the pool.
- For the pre-swap historical pool price, call `eth_call` on the pool with data `0x3850c7bd` (Pancake V3 `slot0()`) and the historical block number **tx_block−1**. Decode the first 32-byte return word as `sqrtPriceX96`, then calculate `(sqrtPriceX96 / 2^96)^2` for BNB per FLAPJAX (both 18-decimal tokens). Checked via the public archive-capable endpoint `https://bsc-mainnet.public.blastapi.io`; some other public BSC nodes returned `missing trie node` and are not archival.
- The **effective** BNB/FLAPJAX price for each actual buy is integer BNB wei paid divided by integer FLAPJAX wei transferred, with decimal scaling cancellation. This differs from instantaneous pool spot price due to swap impact and fees.
- Treasury balance at the historical swap block is checked with `eth_getBalance(treasury, blockNumber)`, and compared against 0.025 BNB. Pool price queries refer to the immediately preceding **block**, not necessarily the immediately preceding intra-block trade.

## Evidence limitations

The earlier audit covered nine independently receipt-verified candidate hashes through Oct 18, and this extension re-read the three new Oct 19–21 candidate hashes from RPC transaction/receipt/block endpoints. The historical pre-swap `slot0()` and treasury balance were fetched independently for **all 12**. Free historical `eth_getLogs` scanning is restricted or rate-limited by public RPC providers (examples: `limit exceeded`, narrow window caps). **The 12 confirmed transactions do not constitute an exhaustive accounting of every pool event or treasury trade.** An archival log/indexed export is needed to prove absence of treasury sells or additional buys. Results below reflect only the transactions positively verified.

Prepared for Taskmarket Receipt Relay Q41. Worker address (BSC-compatible EVM): `0x89728C924b550578866d33E13E4A8618d4d04d28`. Public handle: `@2022117144` (GitHub). This report and its on-chain links are public; no paid buy or promotion was performed.

# API Documentation for DeFi Analytics Platform

## Overview

**DeFi Analytics Platform** provides an API for analyzing DeFi data and sending real-time trading signals. It supports multiple blockchains (Ethereum, Polygon, BSC, Solana, and others), allowing users to track and interact with transactions in decentralized financial systems and smart contracts..

---

## **Base URL**

- Base URL for the API:

```https://api.defi-analytics-platform.com/v1```

## **Authentication**

- The API requires an API key. To authenticate requests, include your API key in the `Authorization` header.

- Example: `Authorization: Bearer YOUR_API_KEY`


---

## Available Endpoints

---

- ### 1. **Get Trading Signal**

- #### Endpoint: `/signal`

- **Method**: `GET`

- **Description**: This endpoint allows users to get the latest trading signals based on market data.

- **Query Parameters**:
- `pair` (string) — The trading pair for which the signal is requested (e.g., `ETH-USDT`).
- `threshold` (float) — The price change threshold to generate a trading signal. Default is 5.0 (5%).

**Response**:
```json
{
  "signal": "Buy ETH",
  "pair": "ETH-USDT",
  "threshold": 5.0,
  "timestamp": "2025-02-09T14:23:00Z"
}
```

### 2. Get Balance

- Endpoint: `/balance`
- Method: `GET`
- Description: This endpoint returns the current balance of a specified address on the selected blockchain.
- Query Parameters:
`address` (string) — The wallet address (e.g., `0x1234567890abcdef...`).
`blockchain` (string) — Блокчейн-сеть (например, `ethereum`, `polygon`, `bsc`).`

#### Response:
```json
{
  "address": "0x1234567890abcdef...",
  "balance": "12345.6789",
  "currency": "USDT"
}
```
### 3. Get Blockchain Data

Endpoint: `/blockchain-data`
Method: `GET`

- Description: This endpoint returns analytics data for the selected blockchain, including transaction volume and trends.

#### Query Parameters:

`blockchain` (string) — The blockchain to analyze (e.g., `ethereum`, `polygon`).

#### Response:
```json
{
  "blockchain": "ethereum",
  "data": {
    "total_transactions": 1234567,
    "total_volume": "5000000",
    "active_addresses": 12000
  }
}
```
### 4. Get Events from Smart Contract

- Endpoint: `/events`
- Method: `GET`

- Description: This endpoint retrieves events (logs) from a specified smart contract on the selected blockchain.
- Query Parameters:

`contract_address` (string) — The smart contract address.
`blockchain` (string) — The blockchain network (e.g., `ethereum`, `polygon`, `bsc`).
`from_block` (number) — The starting block number for event retrieval (optional).
`to_block` (number) — The ending block number for event retrieval (optional)
#### Ответ:
```json
{
  "events": [
    {
      "event_type": "Transfer",
      "data": "0xabcdef123456...",
      "block_number": 1234567
    },
    {
      "event_type": "Approval",
      "data": "0xabcdef987654...",
      "block_number": 1234568
    }
  ]
}
```
### 5. Send Transaction

- Endpoint: `/transaction`
- Method: `POST`

- Description:  This endpoint allows users to send a transaction to a smart contract (e.g., call a function to interact with the contract).

- Параметры тела:
-  `from_address` (string) — The sender address.
- `to_address` (string) — The smart contract address.
- `private_key` (string) — The sender's private key to sign the transaction.
- `amount` (number) — The amount of tokens to send.
- `function` string) — The contract function name (e.g., transfer, approve).
#### Response:

```json
{
  "transaction_hash": "0xabcdef123456...",
  "status": "success",
  "message": "Transaction sent successfully"
}
```

### 6. Subscribe to Events

- Endpoint: `/subscribe`
- Method: `POST`

- Description: This endpoint allows users to subscribe to real-time events for a specific smart contract.

- Body Parameters:

- `contract_address` (string) — The smart contract address.
- `event_type` (string) — The event type to subscribe to (e.g., `Transfer`, `Approval`).
 #### Response:
```json
{
  "status": "subscribed",
  "message": "Subscribed to events successfully"
}
```
### Error Responses

- If an error occurs, the API will return a standard error response.

Example:
```json
{
  "error": {
    "code": 400,
    "message": "Invalid address format"
  }
}
```

### Rate Limiting
- The API uses rate limiting to prevent abuse. Each user can make up to 1000 requests per hour. If the limit is exceeded, a  `429 Too Many Requests.` error will be returned.

#### Пример:

```json
{
  "error": {
    "code": 429,
    "message": "Rate limit exceeded"
  }
}
```
### Conclusion
- This API allows you to integrate with the DeFi Analytics Platform to analyze blockchain data, receive trading signals, monitor smart contracts, and interact with decentralized financial platforms. You can easily extend your capabilities by using the provided endpoints to retrieve and send data in real time.

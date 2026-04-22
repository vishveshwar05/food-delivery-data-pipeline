#  Food Delivery Real-Time Data Pipeline

## 📌 Overview
Built a real-time serverless data pipeline to track food delivery orders using AWS services.

## ⚙️ Architecture
Python → DynamoDB → Streams → Lambda → Kinesis Firehose → S3 → Glue → Athena → QuickSight

## 🛠️ Technologies
- Amazon DynamoDB
- DynamoDB Streams
- AWS Lambda
- Kinesis Firehose
- Amazon S3
- AWS Glue
- Amazon Athena
- Amazon QuickSight

## 🔄 Workflow
1. Orders generated using Python producer
2. Stored in DynamoDB
3. Streams capture real-time events
4. Lambda processes and sends to Firehose
5. Firehose stores data in S3 (bronze layer)
6. Glue transforms to silver layer
7. Athena queries data
8. QuickSight builds dashboards

## 🚀 Key Features
- Real-time event-driven pipeline
- Serverless architecture
- Scalable data processing
- End-to-end analytics system

## 📊 Outcomes
- Real-time order tracking
- Delivery performance analysis
- Business insights dashboard

# Intern Matching System

## Overview
This project builds an end-to-end system for matching interns to open positions, leveraging large language models and other AI techniques. Key components include:

1. Resume processing and structured data extraction
2. Resume embedding and matching using a Qdrant vector database
3. Personalized interview question generation with a Cohere reranker model
4. Candidate evaluation framework with logit biasing and agentic tool use

## Methodology
1. Resume processing using open-source libraries (Unstructured IO)
2. Cross reference resume data via embedding in two domains: "skills" and "domains" using bge-base-en-v1.5
3. Matching candidates to positions using ANN
4. Tailored interview question generation with the Cohere reranker model
5. Robust candidate evaluation framework

## Results and Outcomes
- End to end resume review and candidate evaluation process
- Improved candidate-job matching quality, leading to better hires
- Enhanced candidate experience through personalized assessments

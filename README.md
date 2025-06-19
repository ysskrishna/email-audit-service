# Email Audit Service

A service to evaluate the quality and compliance of email communication between company employees and external customers. The service processes email threads (.eml format) and applies a flexible rules engine to audit them, providing detailed feedback with scoring and justifications.

## Features

- **Dynamic Rules Engine**: Supports multiple rules that can be enabled/disabled:
  - Greeting Rule: Checks for proper email greetings
  - Clarity Rule: Evaluates message clarity and conciseness
  - Grammar Rule: Checks for basic grammar issues
  - Tone Rule: Ensures professional and appropriate tone

- **Comprehensive Audit Reports**:
  - Overall numerical score
  - Pass/fail status per rule
  - Detailed justifications
  - Strengths and areas for improvement

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ysskrishna/email-audit-service.git
cd email-audit-service
```

## Usage

### Run with Docker

```bash
docker-compose up
```

### Command Line Arguments

- `--emails`: One or more .eml files to process
- `--employee-domain`: Domain to identify employee emails (default: @test.com)
- `--rules`: Rules to apply (choices: GREETING, CLARITY, GRAMMAR, TONE)

## Project Structure

```
assessment/
├── core/                   # Core functionality
│   ├── email_parser.py    # Email parsing and processing
│   ├── enums.py          # Enumerations
│   └── types.py          # Data types and models
├── ruleengine/            # Rules implementation
│   ├── engine.py         # Rules engine
│   ├── rule_base.py      # Base rule class
│   └── rules/            # Individual rules
├── data/                  # Sample email files
└── main.py               # CLI entry point
```


### Run Locally

#### Process Multiple Files
```bash
python main.py --emails data/employee_reply_email_with_image_attachment.eml data/employee_reply_email_without_image_attachment.eml --employee-domain @test.com --rules GREETING CLARITY GRAMMAR TONE
```

#### Process Single File with Limited Rules
```bash
python main.py --emails data/employee_reply_email_with_image_attachment.eml --employee-domain @test.com --rules GREETING CLARITY
```
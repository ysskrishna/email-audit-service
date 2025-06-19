# Email Audit Service


## Run Locally

#### Run with multiple files
```bash
python main.py 
  --emails data/employee_reply_email_with_image_attachment.eml data/employee_reply_email_without_image_attachment.eml 
  --employee-domain @test.com 
  --rules GREETING CLARITY GRAMMAR TONE
```

### Run with single file with limited rules
```
python main.py 
  --emails data/employee_reply_email_with_image_attachment.eml
  --employee-domain @test.com 
  --rules GREETING CLARITY
```
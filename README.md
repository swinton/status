# `status`

Check your website status with AWS Lambda.

## Installation

1. Sign up for AWS Lambda
1. Install and configure the `aws` command-line client
1. Run `script/bootstrap`

### Sign up for AWS Lambda

Sign up for AWS [**here**](https://aws.amazon.com/).

The Lambda free tier includes 1M free requests per month and 400,000 GB-seconds of compute time per month.

### Install and configure the `aws` command-line client

To install the `aws` command-line client use `pip`:

```
pip install awscli --upgrade --user
```

To configure `aws`, follow these [**quick configuration steps**](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration).

Once configured, you should see `config` and `credentials` files in `~/.aws`.

### Run `script/bootstrap`

```bash
script/bootstrap
```

This will:

1. Ensure the Lambda function role is created, with the correct policy attached
2. Package the Lambda function and all its dependencies
3. Create the Lambda function on AWS

## Usage

Use the `script/exec_lambda` script.

E.g. to check the status of `https://github.com/`:

```bash
# Check status of github.com
script/exec_lambda status '{"url":"https://github.com/"}'
```

If all is well with your website, you should see:

```json
{
  "url": "https://github.com/",
  "status_code": 200,
  "message": "All is well",
  "ok": true
}
```

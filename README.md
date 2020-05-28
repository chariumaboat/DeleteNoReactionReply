# Delete unresponsive replies daily

If a reply is ignored, delete.
Run daily with AWS Lambda.

- reply to be deleted
  - No Favorite/RT replys
  - No Reply Tweets

## How to deploy
- Precondition
  - Python
  - AWS CLI
  - Twitter API Key

- Includes tweepy(External module) in package

```Powershell
pip install tweepy --target ./code
```

- Packaging

```Powershell
aws cloudformation package --s3-bucket $YourBucketName `
--template-file lambda.yml `
--output-template-file lambda-packaged.yml
```

- Deploy

```Powershell
aws cloudformation deploy `
--template-file lambda-packaged.yml `
--stack-name $YourStackName `
--parameter-overrides AccessSecret=$YourAccessSecret `
ConsumerKey=$YourConsumerKey ` 
ConsumerSecret=$YourConsumerSecret ` 
AccessKey=$YourAccessKey `
--capabilities CAPABILITY_NAMED_IAM
```

## 日本語解説
[Qiitaに書いた](https://qiita.com/harddisking/items/4f61cba9a10a1be7799c)

# STATIC BLOG!

Static Blog is a utility for deploying new versions of a static website to AWS s3, without all that ridiculous manual upload and download nonsense.

### why?

I use <a href="https://docs.aws.amazon.com/AmazonS3/latest/user-guide/static-website-hosting.html">S3 websites</a>, but find source controlled projects tricky to maintain synchronously with S3. Often I'll update a website's source and forget to change it in the bucket, so visitors end up seeing old versions of pages!

This will enable the use of git to source control static pages much more easily, at least for me! I'm building this out to my desired specs, but feel free to fork it or take any of the code within for your own use

### Goals:

[] Upload entire directory of files (maintaining structure) to S3 bucket
[] Auto-deploy option for most recent commit (pre/post-commit hooks?)
[] Preview website locally with SimpleHTTPServer automatically
[] 'Deploy' button on preview page
[] Ability to rollback live site to any commit

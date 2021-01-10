# LayoutDiff Demo project

A Flutter project to demonstrate how to use the LayoutDiff. Feel free to create Pull Requests with layout changes to see it working.

## Dashboard Credentials

You can see changes to be approved on https://app.layoutdiff.com/ using the below account:

username: layoutdiffdemo

password: Example01

## How to send the screenshots with layout changes to demo project

Open a bash on root of this project and execute the follow code:

```bash
export IMAGEPATH=$(pwd)/screenshots/
export PROJECTTOKEN=pLp5yB4RcQVVxsR8inOkQ4rp4qVhWvK5kcYPpTiyaopFb5NZDgxlMtMyVbSb7lonvbKPurSomq171dvyGJZA9bLvfgv7VzuBiExPK3gZwWxMc6m9eZuWU7lZnKfyQABZbVCeWY3R6P3GKxu2iKzlptcxVeDxmU5Wv0yis5yR8iY17LvuNciPzDHlOMMRnLLTwExWCI7J

for filename in $IMAGEPATH/*; do
    curl -X POST -F "image=@$filename" https://app.layoutdiff.com/images/upload/$PROJECTTOKEN/$\( git log | grep -oP 'commit \K[a-f0-9]*' | head -1)
done
```

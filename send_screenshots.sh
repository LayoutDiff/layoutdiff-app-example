#!/bin/bash

# Send screenshots to https://www.layoutdiff.com

export IMAGEPATH=$(pwd)/screenshots/
export PROJECTTOKEN=pLp5yB4RcQVVxsR8inOkQ4rp4qVhWvK5kcYPpTiyaopFb5NZDgxlMtMyVbSb7lonvbKPurSomq171dvyGJZA9bLvfgv7VzuBiExPK3gZwWxMc6m9eZuWU7lZnKfyQABZbVCeWY3R6P3GKxu2iKzlptcxVeDxmU5Wv0yis5yR8iY17LvuNciPzDHlOMMRnLLTwExWCI7J

for filename in $IMAGEPATH/*; do
    curl -X POST -F "image=@$filename" https://app.layoutdiff.com/images/upload/$PROJECTTOKEN/$GITHUB_SHA
done

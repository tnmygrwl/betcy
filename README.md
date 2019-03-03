# Betcy
## Inspiration
*How many times your friend has made a bet with you and never really came through?*

## What it does
It helps you to easily create an *immutable* bet between you and your friend with a wager as a Macy's Product using Amazon Alexa.

## How we built it

We built a skill for amazon Alexa using their developer console and used amazon lambda services to deploy it and seamlessly connect it with the web server. We used smart contracts to create an immutable bet between two friends having Macy's products as a wager. We used Macy's catalog-services-api to achieve the same. The web-app is made with vue.js for frontend and we used node.js for backend and integrating it with the ethereum framework.

## Challenges we ran into

Some of the challenges we ran into were:
<ol>
<li>Deploying it on amazon Alexa and integrating it with the frontend. </li>
<li>Working with web3.js on a vue.js component. </li>
<li>Bypassing cross-origin resource sharing for HTTP request via XHR.</li>
</ol>

## Accomplishments that we're proud of

Ability to deploy smart contracts on an ethereum testnet just using Alexa voice commands.

## What we learned

While the individual components work perfectly on their own, integrating it and *bringing* together the product as a whole is a huge challenge.

## What's next for Betcy
<ol>
<li>Improving the user experience and scalability.</li>
<li>Coming up with a viable business model.</li>
<li>And keep on asking *"What's Next?"*</li>
</ol>


## Our Website
```
http://www.betcy.com/
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

const path = require('path');
const BundleTracker = require("webpack-bundle-tracker");

const VueConfig = {
  css: {
    sourceMap: true
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/'
    : 'http://127.0.0.1:8080',
  outputDir: path.resolve(__dirname, '../static/'),

  chainWebpack: (config) => {
    config.optimization
    .splitChunks(false);

    config
    .plugin('BundleTracker')
    .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}]);

    config.resolve.alias
    .set('__STATIC__', 'static');

    config.devServer
    .public('http://127.0.0.1:8080')
    .host('127.0.0.1')
    .port(8080)
    .hotOnly(true)
    .watchOptions({poll: 1000})
    .https(false)
    .headers({"Access-Control-Allow-Origin": ["\*"]});
  }
};

module.exports = VueConfig;

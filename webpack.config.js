const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const CleanWebpackPlugin = require('clean-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');

const outputPath = __dirname + '/static/dist/';

const path = require('path');


// the path(s) that should be cleaned
let pathsToClean = [outputPath];

let commonsPlugin = new webpack.optimize.CommonsChunkPlugin({name: 'common', filename: 'js/common.bundle-[hash].js'});

module.exports = {
  entry: {
    landing: "./src/landing.js",
    app: "./src/stats.js",
  },
  output: {
    path: outputPath,
    publicPath: '/static/dist/',
    filename: "js/[name].bundle-[hash].js"
  },
  module: {
    rules: [
      {
        test: /\.s?css$/,
        use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader!sass-loader"
        })
      },
      { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=10000&mimetype=application/font-woff" },
      { test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader" }
    ]
  },
  plugins: [
    new CleanWebpackPlugin(pathsToClean),
    commonsPlugin,
    new ExtractTextPlugin({filename: 'css/[name]-[hash].css', allChunks: true}),
    new BundleTracker({filename: './webpack-stats.json'}),
  ]
};
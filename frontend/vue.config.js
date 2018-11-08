var path = require('path');

// vue.config.js
module.exports = {
  outputDir: path.resolve(__dirname, '../templates/vue'),
  assetsDir: '../../static',
  indexPath: 'index.html',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true
      }
    },
  }
}
const express = require('express');
const router = express.Router();

router.get('/settings', (req, res) => {
  res.render('settings', { title: 'Settings' });
});

module.exports = router;
const express = require('express');
const router = express.Router();

router.get('/dark-mode', (req, res) => {
  res.render('dark_mode');
});

module.exports = router;
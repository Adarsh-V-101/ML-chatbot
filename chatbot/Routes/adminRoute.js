const express = require('express')
const admincontroll = require('../controller/admincontrol.js')
const router = express.Router()

router.get('/admin',admincontroll.adminPage)

module.exports = router
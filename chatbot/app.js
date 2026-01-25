const express = require('express')
const router = require('./Routes/adminRoute.js')
const ejs = require('ejs')

const app = express()
app.set('view engine',ejs)
app.use(express.json())

app.get('/admin',router)
app.get('/',(req,res)=>{
    res.send('hell world')
})
app.listen(3000)


var buck_data = {isNew:0,/*id:0,*/analogSignal:0,digitalSignal:0}

//接收数据
exports.accept_data = (req,res)=>{
    buck_data.isNew = 1
    // buck_data.id =  req.body.id
    buck_data.analogSignal =  req.body.analogSignal
    buck_data.digitalSignal =  req.body.digitalSignal
    //console.log(buck_data)
    return res.cc("success accept",0)
}
//向前端发数据
exports.sent_data = (req,res)=>{
    if(!buck_data.isNew) {
        return res.cc("no new info")
    }
    buck_data.isNew = 0
    //console.log(buck_data)
    return res.send({status:0,data:buck_data})
}


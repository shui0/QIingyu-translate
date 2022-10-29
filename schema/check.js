// 导入joi模块，定义效验规则
const { ref, required } = require('joi')
const joi = require('joi')

const analogSignal = joi.number().required()//模拟信号
const digitalSignal = joi.number().required()//数字信号
const id =  joi.number().required()//唯一标识id
const imgNameCheck = joi.string().required()//图片文件名

exports.sent_them = {
    body:{
        // id ,
        analogSignal ,
        digitalSignal ,
    },
}

exports.sentimgName = {
    body:{
        imgNameCheck,
    }
}

var host="http://127.0.0.1:5098"
var serverUrl_show = host+"/select/form/";//显示数据
var serverUrl_add =  host+"/insert/";//添加数据
var serverUrl_edit =  host+"/update/";//修改数据
var serverUrl_del =  host+"/update/";//删除数据
var serverUrl_login = host+"/select/";//显示数据
var serverUrl =  host;//添加数据
var serverUrl_down= host+"/download/";
document.write("<script language=javascript src='../student/js/axios.js'></script>");
document.write("<script language=javascript src='../student/js/eleindex.js'></script>");
//axios_post请求
function send_post(data,vm) {
    //var send_data = Object.assign({}, data);
    var send_data=obj_to_obj(data);
    delete send_data["url"];
    // var path_bool=send_data.hasOwnProperty("path");
    // if (path_bool) {
    //     delete send_data["path"];
    // }
    var e_msg_bool=send_data.hasOwnProperty("e_msg");
    if (e_msg_bool==false) {
        data["e_msg"]="数据获取失败";
    }
    axios({
        method: 'post',
        url: host + data.url,
        data: send_data,
    })
        .then(function (response) {
            if (response.data.code == 1) {
                // if (path_bool) {
                //     window.location = data["path"];
                // }
                return response
            } else {//判断状态码
                vm.$message({
                    showClose: true,
                    message:data["e_msg"],
                    type: 'error'
                });
                return response
            }
        })
        .catch(function (error) {//请求失败事件
            vm.$message({
                showClose: true,
                message: '恭喜你,请求错误了',
                type: 'error'
            });
        })
}
//obj转json字符串，再转对象
function obj_to_obj(obj) {
    var obj3 = JSON.parse(JSON.stringify(obj));//先将obj转换为JSON字符串，然后再转回对象
    return obj3
}
//axios_get请求
function send_get(data,url,vm,) {
    var url_val="?";
    for(var key in data){
        url_val=url_val+key+"="+data[key]+"\&";
    }
    var u_data=url_val.slice(0,url_val.length-1);
    axios({
        method: 'get',
        url: host + url+u_data,
    })
        .then(function (response) {
            if (response.data.code == 1) {

                return response
            } else {//判断状态码
                vm.$message({
                    showClose: true,
                    message:data["e_msg"],
                    type: 'error'
                });
                return response
            }
        })
        .catch(function (error) {//请求失败事件
           alert(error);
        })
}

var json_data=[{"path":"teachsource.html","class":"el-icon-setting","name":"教学资源管理"}]
function r_menu(json_data) {
    var data='<div class=\"layui-side layui-bg-black\"> <div class=\"layui-side-scroll\"> <ul class=\"layui-nav layui-nav-tree\" lay-filter=\"test\">';
    // json_data.forEach(function (element, index, array) {
    //
    // })
}
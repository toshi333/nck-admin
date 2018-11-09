import axios from 'axios'

export default {
    //一覧取得
    list(url, key) {
        return new Promise((resolve) => {
            axios.get(url + key)
                .then((res) => {
                    resolve(res.data)
                })
                .catch((error) => {
                    reject(error)
                })
        })
    },

    create(url, data, contentType=null) {
        let sendOptions = { headers: { 'X-CSRFToken': this.csrftoken("csrftoken") } }
        if(contentType) sendOptions.headers['content-type'] = contentType
        return new Promise((resolve, reject) => {
            axios.post(url, data, sendOptions)
                .then(
                    resolve()
                )
                .catch((error) => {
                    reject(error)
                })
        })
    },

    update(url, key, data, contentType=null) {
        let sendOptions = { headers: { 'X-CSRFToken': this.csrftoken("csrftoken") } }
        if(contentType) sendOptions.headers['content-type'] = contentType

        return new Promise((resolve, reject) => {
            axios.put(url + key + '/', data, sendOptions)
                .then(res => {
                    resolve(res)
                })
                .catch((error) => {
                    reject(error)
                })
        })
    },

    delete(url, key) {
        let sendOptions = { headers: { 'X-CSRFToken': this.csrftoken("csrftoken") } }
        return new Promise((resolve, reject) => {
            axios.delete(url + key + '/', sendOptions)
                .then(res => {
                    resolve(res)
                })
                .catch((error) => {
                    reject(error)
                })
        })
    },

    // 新規登録か更新の判断はidフィールドを決め打ちで指定
    // 基本idがデータベースモデルの主キーのはずだが、違っていたら要調整
    save(url, data) {
        if (data.id) {
            return this.update(url, data.id, data)
        } else {
            return this.create(url, data)
        }
    },

    //CSRFトークンを作る関数
    csrftoken() {
        let c_name = "csrftoken"
        if (document.cookie.length > 0) {
            let c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1) {
                c_start = c_start + c_name.length + 1;
                let c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start, c_end));
            }
        }
        return "";
    }
}
<template>
    <div>
        <p>아이디 : {{ userInfo.username }}</p>
        <p>좋아하는 영화 : {{ userInfo.like_movies }}</p>
        <p>좋아하는 리뷰: {{ userInfo.like_reviews }}</p>
        <p>작성 리뷰 : {{ userInfo.reviews }}</p>
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    data() {
        return {
            userInfo: null,
        }
    },
    created() {
        this.getUserDetail()
    },
    methods: {
        getUserDetail() {
            axios({
                method : 'get',
                url : `${API_URL}/mypage/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
            .then((res) => {
                this.userInfo = res.data
            })
            .catch((err) => {
                console.log(err)
            })
        }
    }
}
</script>

<style>

</style>
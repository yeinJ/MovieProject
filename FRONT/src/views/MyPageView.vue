<template>
    <div>
        <BasicInfo
        v-bind:username="userInfo?.username"/>
        <LikedMovie
        v-bind:movies="userInfo?.like_movies"/>
        <br>
        <br>
        <WrittenReview
        v-bind:reviews="userInfo?.reviews"/>
    </div>
</template>

<script>
import BasicInfo from '@/components/MyPage/BasicInfo.vue'
import LikedMovie from '@/components/MyPage/LikedMovie.vue'
import WrittenReview from '@/components/MyPage/WrittenReview.vue'

import axios from 'axios'
const API_URL = 'http://3.39.173.99:8000'

export default {
    components: {
        BasicInfo,
        LikedMovie,
        WrittenReview,
    },
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

<style scoped>
div{
    margin-bottom: 5%;
    padding : 2%;
}

</style>
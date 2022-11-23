<template>
  <div>
    <hr>
    <h3>작성한 리뷰</h3>
    <div class="header">
    <table>
      <thead>
        <tr>
          <!-- <th>Review List</th> -->
          <th class="trtitle">title</th>
          <th class="trcontent">content</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="content">
    <table>
      <tbody>
        <!-- <td>{{review}}</td> -->
        <div v-for="review in reviews" v-bind:key="review.id">
          <div class="balloon-left">
            <div class="leftmovie">
              
              <router-link class="h4 mb-2" v-bind:to="{name: 'DetailView', params:{id: review.movie}}">
                <b-icon icon="search"></b-icon>
              </router-link>
            </div>
            <!-- <div>{{review.id}}</div> -->
            <div class="centertitle">{{review.title}} </div>
            <div class="rightcontent">{{review.content}}</div>
          </div>

        </div>

      </tbody>
    </table>
  </div>

  </div>
</template>

<script>
export default {
  data() {
    return{
      items : this.reviews
    }
  },
  props: ['reviews'],
  methods: {
  }

  
}
</script>

<style scoped>

h1{
  font-size: 30px;
  color: #fff;
  text-transform: uppercase;
  font-weight: 300;
  text-align: center;
  margin-bottom: 15px;
}
table{
  width:100%;
}
.header{
  background-color: rgba(168, 168, 168, 0.3);
 }
.content{
  height:300px;
  padding-right:3%;
  overflow-x:auto;
  margin-top: 0px;
  border: 1px solid rgba(255,255,255,0.3);
}
th{
  padding: 20px 15px;
  text-align: center;
  font-weight: 500;
  font-size: 12px;
  color: #fff;
  text-transform: uppercase;
}
tbody div{
 /* border-left: 10px solid transparent; 

 border-bottom: 10px solid ;
  
  display:flex;
  justify-content: space-between;
  padding: 15px;
  text-align: left;
  vertical-align:middle;
  font-weight: 300;
  font-size: 12px;
  color: #fff; */
  /* border-bottom: solid 1px rgba(255,255,255,0.1); */
}

.balloon-left {
  position: relative;
  display: flex;
  /* justify-content: space-between; */
  margin: 1.5% 0% 1.5% 3%;
  padding: 1.5% 5%;
  /* min-width: 120px; */
  /* max-width: 100%; */
  color: white;
  font-size: 16px;
  background: #555;
  border: solid 3px #555;
  /* box-sizing: border-box; */
  opacity: 60%;
}
.leftmovie{
  position:relative;
  left : 2%;
  
}
.centertitle{
  position:absolute;
  left : 15%;
  width: 20%;

}
.rightcontent{
  position:relative;
  left : 55%;
  width: 40%;

}


.balloon-left:before {

  position: absolute;
  /* top: 50%;
  left: -24px; */
  margin-top: -12px;
  border: 12px solid transparent;
  border-right: 12px solid #555;
  z-index: 2;
  opacity:60%;

}

.balloon-left:after {
  content: "";
  position: absolute;
  top: 50%;
  left: -30px;
  margin-top: -14px;
  border: 14px solid transparent;
  border-right: 14px solid #555;
  z-index: 1;
}

.balloon-left p {
  margin: 0;
  padding: 0;
}

.trtitle{

}

.trcontent{

}



/* .reviewBox{
  border: 1px solid gray;
  border-radius: 5%;
} */

/* demo styles */

@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
body{
  background: -webkit-linear-gradient(left, #25c481, #25b7c4);
  background: linear-gradient(to right, #25c481, #25b7c4);
  font-family: 'Roboto', sans-serif;
}
section{
  margin: 50px;
}


/* follow me template */
.made-with-love {
  margin-top: 40px;
  padding: 10px;
  clear: left;
  text-align: center;
  font-size: 10px;
  font-family: arial;
  color: #fff;
}
.made-with-love i {
  font-style: normal;
  color: #F50057;
  font-size: 14px;
  position: relative;
  top: 2px;
}
.made-with-love a {
  color: #fff;
  text-decoration: none;
}
.made-with-love a:hover {
  text-decoration: underline;
}


/* for custom scrollbar for webkit browser*/

::-webkit-scrollbar {
    width: 6px;
} 


</style>
<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <h1 class="title">Thank you! </h1>

            <p>Your order will be processed within 48 hours</p>
        </div>
    </div>

</template>

<script>
    export default {
        name: 'Success',
        mounted(){
            document.title = 'Success | Dawesome'
        },
    }
</script>
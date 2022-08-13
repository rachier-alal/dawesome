<template>

    <tr class="is-full-width">
        <td><routre-link :to="item.product.get_absolute_url">{{ item.product.name }}</routre-link></td>
        <td>Ksh. {{ item.product.price }}</td>
        <td>{{ item.quantity }}</td>
        <td>Ksh. {{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete"></button></td>
    </tr>
</template>
<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
    }
    
}
</script>
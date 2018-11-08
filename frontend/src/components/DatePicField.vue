<template>
    <div>
        <v-menu
                :close-on-content-click="false"
                v-model="menu"
                :nudge-right="40"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
        >
            <v-text-field
                    slot="activator"
                    v-model="internalValue"
                    :label="label"
                    prepend-icon="event"
                    v-on:input="$emit('input', $event.target.value)"
                    readonly
            ></v-text-field>
            <v-date-picker v-model="internalValue" locale="ja" no-title scrollable
                           @input="menu = false"></v-date-picker>
        </v-menu>
    </div>
</template>

<script>

export default {
  name: 'DataPicField',
  props: ['label', 'value'],
  data () {
    return {
        menu: false,
    }
  },
  computed: {
    internalValue: {
      get () {
        return this.value
      },
      set (newVal) {
        if (this.value !== newVal) this.$emit('input', newVal)
      }
    }
  }
}


</script>
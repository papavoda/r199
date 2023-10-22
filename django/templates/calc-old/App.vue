const App = {
    data() {
        return {
            title: 'Список заметок',
            placeholderString: 'Введите название заметки',
            inputValue: "",
            notes: ['Заметка 1', 'Заметка 2']

        }
    },
    methods: {
        addNewNote() {
            if (this.inputValue){
                this.notes.push(this.inputValue)

            }
            this.inputValue = ''
        },
        toUpperCase(item){
          return item.toUpperCase()
        },
        removeNote(index) {
            // console.log(index)
            this.notes.splice(index, 1)
        }
    },
    computed: {
        doubleCountComputed(){
            // console.log('doubleCountComputed')
            return this.notes.length * 2
        }
    },
    watch: {
        inputValue(value){
            // console.log('Input value changed: ', value)
            if (value.length > 10) {
                this.placeholderString = 'Максимальное количество 10 символов'
                this.inputValue = ''
            }
        }
    }
}

Vue.createApp(App).mount("#app")


const App0 = {
    // метод
    data() {
        // возвращаем объект
        return {
            counter: 0,
            title: 'Счетчик'
        }
    }
}

Vue.createApp(App0).mount("#app0")

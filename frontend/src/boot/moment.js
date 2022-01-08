import { boot } from 'quasar/wrappers'


export default boot(({ app }) => {
    app.use(require('vue-moment'));
})

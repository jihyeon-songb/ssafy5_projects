export default {
  LOGOUT(state) {
    state.isUser = false
    state.initNickname = ''
    state.initProfileimg = ''
    state.token = ''
    state.uid = ''
    state.filePath = ''
    state.nickname = ''
    state.email = ''
    state.emailCompany = ''
    state.hasSurveyed = false
  },
  LOGIN(state, user) {
    state.email = user.email
    state.emailCompany = user.emailCompany
    state.filePath = user.filePath
    state.hasSurveyed = user.hasSurveyed
    state.nickname = user.nickname
    state.uid = user.uid
  },
  SAVE_TOKEN(state, token) {
    state.token = token
  },
  CHANGEPROFILE(state, user) {
    state.nickname = user.nickname
    state.filePath = user.filePath
  },
}

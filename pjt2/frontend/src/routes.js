import PageNotFound from './views/error/PageNotFound.vue'
import Login from './views/user/Login.vue'
import InitNickname from './views/user/InitNickname.vue'
import InitProfileImg from './views/user/InitProfileImg.vue'
import Profile from './views/profile/Profile.vue'
import MyInfo from './views/profile/MyInfo.vue'
import MyInfoUpdate from './views/profile/MyInfoUpdate.vue'
import MyDiary from './views/profile/MyDiary.vue'
import MyPlaylist from './views/profile/MyPlaylist.vue'
import DiaryReport from './views/profile/DiaryReport.vue'
import EmotionReport from './views/profile/EmotionReport.vue'
import SurveyStart from './views/survey/SurveyStart.vue'
import Survey from './views/survey/Survey.vue'
import Components from './views/Components.vue'
import Main from './views/main/Main.vue'
import CreateDiary from './views/diary/CreateDiary.vue'
import ReadDiary from './views/diary/ReadDiary.vue'
import UpdateDiary from './views/diary/UpdateDiary.vue'
import Music from './views/diary/Music.vue'

export default [
  {
    path: '/',
    name: 'Login',
    component: Login,
    meta: { auth: false },
  },
  {
    path: '/components',
    name: 'Components',
    meta: { auth: true },
    component: Components,
  },
  {
    path: '/user/nickname',
    name: 'InitNickname',
    meta: { auth: true },
    component: InitNickname,
  },
  {
    path: '/user/profileimg',
    name: 'InitProfileImg',
    meta: { auth: true },
    component: InitProfileImg,
  },
  {
    path: '/profile',
    name: 'Profile',
    meta: { auth: true },
    component: Profile,
  },
  {
    path: '/profile/myinfo',
    name: 'MyInfo',
    meta: { auth: true },
    component: MyInfo,
  },
  {
    path: '/profile/myinfo/update',
    name: 'MyInfoUpdate',
    meta: { auth: true },
    component: MyInfoUpdate,
  },
  {
    path: '/profile/mydiary',
    name: 'MyDiary',
    meta: { auth: true },
    component: MyDiary,
  },
  {
    path: '/profile/myplaylist',
    name: 'MyPlaylist',
    meta: { auth: true },
    component: MyPlaylist,
  },
  {
    path: '/profile/mydiaryreport',
    name: 'DiaryReport',
    meta: { auth: true },
    component: DiaryReport,
  },
  {
    path: '/profile/emotionreport',
    name: 'EmotionReport',
    meta: { auth: true },
    component: EmotionReport,
  },
  {
    path: '/survey',
    name: 'SurveyStart',
    meta: { auth: true },
    component: SurveyStart,
  },
  {
    path: '/survey/:survey_num',
    name: 'Survey',
    component: Survey,
    meta: { auth: true },
    props: true,
  },
  {
    path: '/main',
    name: 'Main',
    meta: { auth: true },
    component: Main,
  },
  {
    path: '/diary/:date/create',
    name: 'CreateDiary',
    meta: { auth: true },
    component: CreateDiary,
  },
  {
    path: '/diary/:date',
    name: 'ReadDiary',
    meta: { auth: true },
    component: ReadDiary,
  },
  {
    path: '/diary/:date/update',
    name: 'UpdateDiary',
    meta: { auth: true },
    component: UpdateDiary,
  },
  {
    path: '/diary/:date/:diaryid/music',
    name: 'MusicDiary',
    meta: { auth: true },
    component: Music,
  },
  {
    path: '*',
    redirect: '/404',
  },
  {
    path: '/404',
    name: 'PageNotFound',
    component: PageNotFound,
  },
]

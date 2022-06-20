/*
 * Copyright (C) 2016-present, Yuansuan.cn
 */

import { Rule } from 'antd/lib/form'

// import Item from 'antd/lib/list/Item'

export enum ParamComponent {
  'Input',
  'Select',
  'MultiSelect',
  'Radio',
  'Switch',
  'Checkbox',
  'Upload',
  'InputNumber',
  'SelectTool',
  'GridSelect',
  'InputGas',
  'SelectGas',
  'Password',
  'SelectRoleGroup',
}

export enum SettingComponent {
  'Turbulence',
  'SiderBar',
  'SpaceBar',
  'Common',
}

export interface ParamProps {
  label: string
  key: string
  type?: ParamComponent
  options?: ([string, any] | string | {} | [object])[]
  visible?: boolean
  props?: SubParamProps[]
  defaultValue?: string
  group?: string[]
  box?: string
  rules?: Rule & { message: string }[]
}

interface ChildrenParams {
  label: string
  key: string
  type?: ParamComponent | string
  options?: ([string, any] | string | {})[] | any
  showStatus?: string
  rules?: Object[]
}

export interface SubParamProps {
  type: string
  key: number
  subkey?: number
  params?: ChildrenParams[]
}

type ProjectParam = ParamProps & {
  // 是否可在提交作业页面编辑
  editable?: boolean
  disabled?: boolean
  // 全局参数｜网格参数
  namespace?: 'global' | 'grid'
}
export const userGroup = [
  {
    label: '用户组名称',
    type: ParamComponent.Input,
    key: 'usergroup_name',
    rules: [
      { required: true, message: '请输入用户组名' },
      { type: 'string', whitespace: true, message: '用户组名不能是空格' },
    ],
  },
  {
    label: '用户组描述',
    type: ParamComponent.Input,
    key: 'usergroup_desc',
    rules: [{ required: false, message: '请输入用户组描述' }],
  },
]

export const userParams = [
  {
    label: '昵称',
    type: ParamComponent.Input,
    key: 'user_name',
    rules: [
      { required: true, message: '请输入用户昵称' },
      { type: 'string', whitespace: true, message: '用户昵称不能是空格' },
    ],
  },
  {
    label: '真实姓名',
    type: ParamComponent.Input,
    key: 'user_real_name',
    rules: [
      { required: true, message: '请输入用户真实姓名' },
      { type: 'string', whitespace: true, message: '真实姓名不能是空格' },
    ],
    disabled: true,
  },
  {
    label: '邮箱',
    type: ParamComponent.Input,
    key: 'user_email',
    rules: [
      { required: false, message: '请输入用户邮箱' },
      {
        pattern:
          /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/,
        message: '邮箱格式不正确',
      },
      {
        max: 50,
        message: '邮箱不得超过50字符',
      },
    ],
  },
  {
    label: '手机号',
    type: ParamComponent.Input,
    key: 'user_phone',
    rules: [
      { pattern: /^1[3|4|5|7|8][0-9]\d{8}$/, message: '请输入正确的手机号' },
      { required: false, message: '请输入用户手机号' },
    ],
  },
  {
    label: '角色',
    type: ParamComponent.SelectRoleGroup,
    key: 'user_role_id',
    rules: [
      {
        required: true,
        message: '请选择用户角色',
      },
    ],
    options: [],
  },
  {
    label: '用户组',
    type: ParamComponent.SelectRoleGroup,
    key: 'user_org_id',
    rules: [
      {
        required: true,
        message: '请选择用户组',
      },
    ],
    options: [],
  },
  {
    label: '状态',
    type: ParamComponent.Switch,
    key: 'user_status',
    rules: [{ required: true, message: '请输入用户状态' }],
  },
  {
    label: '密码',
    type: ParamComponent.Password,
    key: 'user_pass',
    rules: [
      {
        required: true,
        message: '请输入用户密码',
      },
      {
        pattern: /^[\w_-]{6,16}$/,
        message: '用户密码不符合规则',
      },
    ],
  },
  {
    label: '确认密码',
    type: ParamComponent.Password,
    key: 'user_confirmPass',
    rules: [
      {
        required: true,
        message: '请输入用户确认密码',
      },
      ({ getFieldValue }) => ({
        validator: (_, value) => {
          if (value && getFieldValue('user_pass') === value) {
            return Promise.resolve()
          }
          return Promise.reject('用户密码俩次输入不一致')
        },
      }),
    ],
  },
]

export const projectParams: ProjectParam[] = [
  {
    label: '工程名称',
    type: ParamComponent.Input,
    key: 'name',
    rules: [
      { required: true, message: '请输入你的工程名称' },
      { type: 'string', whitespace: true, message: '工程名称不能是空格' },
    ],
  },
  {
    label: '模式选择',
    options: [
      ['低速流动', 0],
      ['跨声速流动', 1],
      ['高超声速流动', 2],
    ],
    type: ParamComponent.Radio,
    key: 'type',
  },
  {
    label: '空间维度',
    options: [
      ['二维', 2],
      ['三维', 3],
    ],
    type: ParamComponent.Radio,
    key: 'ndim',
    editable: true,
    disabled: true,
  },
  {
    label: '求解器',
    options: [
      ['非结构', 0],
      ['结构', 1],
    ],
    type: ParamComponent.Radio,
    key: 'gridtype',
    editable: true,
    disabled: true,
  },
  {
    label: '参数模式',
    options: [
      ['标准', 0],
      ['高级', 1],
    ],
    type: ParamComponent.Radio,
    key: 'mode',
    editable: true,
  },
  {
    label: '网格格式',
    options: [
      ['*.fts, HyperFLOW (PHengLEI)', 1],
      ['*.cgns, CGNS', 2],
      ['*.dat/*.grd/*.inp, Plot3D type of structured grid', 3],
      ['*.dat/*.inp, Fieldview type of unstructured grid', 4],
      ['*.cas/*.msh, Fluent', 5],
      ['mgrid.in, Ustar', 6],
      ['*.fts, Hybrid, include both of unstructured and structured grid', 7],
      ['*.msh, GMSH', 8],
    ],
    type: ParamComponent.GridSelect,
    key: 'from_gtype',
    rules: [
      { required: true, message: '请输入你的工程名称' },
      ({ getFieldValue }) => ({
        validator: async (_, value) => {
          const filelist = getFieldValue('from_gfile')
            ? getFieldValue('from_gfile')?.fileList?.map(
                i => `.${i.name.split('.')[1]}`
              )
            : []
          const from_gtype = projectParams[5].options
            .find(i => i[1] == value)[0]
            .match(/.(\S*),/)[1]
            .replace(/\*/g, '')
            .replace(new RegExp('/', 'g'), ',')
            .split(',')
          from_gtype.push('.undefined')
          filelist.forEach(element => {
            if (!from_gtype.includes(element)) {
              throw new Error('网格格式与上传网格文件格式不符')
            }
          })
        },
      }),
    ],
  },
  {
    label: '网格单位',
    options: [
      ['米(m)', 0],
      ['分米(dm)', 1],
      ['厘米(cm)', 2],
      ['毫米(mm)', 3],
      ['英寸(inch)', 4],
      ['英尺(foot)', 5],
      ['码(yard)', 6],
    ],
    type: ParamComponent.GridSelect,
    key: 'gridUnit',
  },
  {
    label: '网格方向',
    options: [
      ['y轴向上', 1],
      ['z轴向上', 2],
    ],
    type: ParamComponent.Radio,
    key: 'axisup',
  },
  {
    label: '进程数目',
    type: ParamComponent.Input,
    key: 'maxproc',
    namespace: 'grid',
    rules: [
      { required: true, message: '请输入你的进程数目' },
      {
        pattern: new RegExp(/^[1-9]\d*$/, 'g'),
        message: '进程数只能是大于0的整数',
      },
    ],
  },
  {
    label: '源网格',
    type: ParamComponent.Upload,
    key: 'from_gfile',
    rules: [
      { required: true, message: '请上传你的网格文件' },
      ({ getFieldValue, validateFields }) => ({
        validator: (_, value) => {
          validateFields(['from_gtype'])
          return Promise.resolve()
        },
      }),
    ],
  },
].map(
  item =>
    ({
      ...item,
      namespace: item.namespace || 'global',
      editable: item.editable === undefined ? false : item.editable,
    } as ProjectParam)
)

export const projectParamsMapper = projectParams.reduce((acc, item) => {
  acc[item.key] = {}
  ;(item.options || []).map(opt => {
    if (typeof opt === 'string') {
      acc[item.key][opt] = opt
    } else {
      acc[item.key][opt[1]] = opt[0]
    }
  })

  return acc
}, {})

export const turbulenceParams: ParamProps[] = [
  {
    label: '定常/非定常',
    options: [
      ['定常', 0],
      ['非定常', 1],
    ],
    type: ParamComponent.Radio,
    key: 'iunsteady',
    group: ['gas'],
  },
  {
    label: '粘性控制',
    options: [
      ['无粘', 0],
      ['层流', 1],
      ['湍流', 3],
    ],
    type: ParamComponent.Select,
    key: 'iviscous',
    group: ['gas'],
  },
  {
    label: '湍流模型',
    options: [
      ['SA模型', '1eq-sa'],
      ['KW-SST模型', '2eq-kw-menter-sst'],
    ],
    type: ParamComponent.SelectTool,
    key: 'visname',
    group: ['gas'],
  },
  {
    label: '湍流间隔步数',
    type: ParamComponent.InputNumber,
    key: 'turbInterval',
    group: ['gas'],
    rules: [{ min: 0, type: 'number', message: '湍流间隔步数不能小于0' }],
  },
  {
    label: '最大迭代步数',
    type: ParamComponent.InputNumber,
    key: 'maxsimustep',
    group: ['gas'],
    rules: [
      { required: true, message: '请输入你的最大迭代步数' },
      { min: 0, type: 'number', message: '最大迭代步数不能小于0' },
    ],
  },
  {
    label: '湍流离散格式',
    type: ParamComponent.SelectTool,
    key: 'n_turb_scheme',
    options: [
      ['roe', 'roe'],
      ['center', 'center'],
      ['nnd', 'nnd'],
    ],
    group: ['gas'],
    rules: [
      { required: true, message: '请输入你的最大迭代步数' },
      { min: 0, type: 'number', message: '最大迭代步数不能小于0' },
    ],
  },
  {
    label: '湍流变量最小系数',
    type: ParamComponent.InputNumber,
    key: 'turb_min_coef',
    group: ['gas'],
    rules: [{ min: 0, type: 'number', message: '湍流间隔步数不能小于0' }],
  },
  {
    type: ParamComponent.Radio,
    key: 'mod_turb_res',
    label: '残差修正',
    options: [
      ['关闭', 0],
      ['打开', 1],
    ],
    group: ['gas'],
  },
  {
    label: '气体类型',
    options: [
      ['完全气体', 0],
      ['非平衡气体', 1],
    ],
    type: ParamComponent.Select,
    key: 'nchem',
    group: ['gas'],
  },
  {
    label: '无量纲时间步长',
    type: ParamComponent.InputNumber,
    key: 'physicalTimeStep',
    group: ['gas'],
    rules: [{ required: true, message: '请输入你的无量纲时间步长' }],
  },
  {
    label: '气体化学反应模型',
    options: [
      ['Gupta模型5组分', 'Gu5'],
      ['Gupta模型7组分', 'Gu7'],
      ['Gupta模型11组分', 'Gu11'],
      ['Park模型5组分', 'Pa5'],
      ['Park模型7组分', 'Pa7'],
      ['Park模型11组分', 'Pa11'],
      ['Dunn-Kang模型5组分', 'DK5'],
      ['Dunn-Kang模型7组分', 'DK7'],
      ['Dunn-Kang模型11组分', 'DK11'],
    ],
    type: ParamComponent.SelectGas,
    key: 'gasfile',
  },
  {
    label: '化学源项',
    options: [
      ['有', 1],
      ['无', 0],
    ],
    type: ParamComponent.Select,
    key: 'nchemsrc',
  },
  {
    label: '源项计算方式',
    options: [
      ['显式', 1],
      ['隐式', 0],
    ],
    type: ParamComponent.Select,
    key: 'nchemrad',
  },
  {
    label: '热力学温度模型',
    options: [
      ['单温度', 1],
      ['双温度', 2],
      ['三温度', 3],
    ],
    type: ParamComponent.Select,
    key: 'ntmodel',
  },
  {
    label: '来流震动温度',
    type: ParamComponent.InputNumber,
    key: 'freestream_vibration_temperature',
    rules: [{ required: true, message: '请输入你的来流震动温度' }],
  },
  {
    label: '壁面催化特性',
    options: ['完全催化', '非催化', '有限催化'],
    type: ParamComponent.Select,
    key: 'catalyticCoefType',
  },
  {
    label: '壁面催化系数',
    type: ParamComponent.InputGas,
    key: 'catalyticCoef',
    rules: [
      { required: true, message: '输入壁面催化系数(0.0-1.0)' },
      { min: 0, type: 'number', message: '请输入大于0的数' },
      { max: 1, type: 'number', message: '请输入小于1的数' },
    ],
  },
]

export const BcTypeProps: SubParamProps[] = [
  {
    type: '外插边界条件',
    key: 1,
  },
  {
    type: '物面边界条件',
    key: 2,
    params: [
      {
        label: '壁面类型',
        options: [
          ['绝热壁', 0],
          ['等温壁', 1],
        ],
        type: 'Select',
        key: 'twall_type',
      },
      {
        label: '壁面温度(K)',
        options: ['-1.0', 0],
        type: 'Input',
        key: 'twall',
        showStatus: 'twall_type',
        rules: [],
      },
      {
        label: '设置参考数据',
        options: [
          ['是', 1],
          ['否', 0],
        ],
        type: 'CheckBox',
        key: 'rePara',
      },
      {
        label: '参考长度l(m)',
        options: ['-1.0', 0],
        type: 'Input',
        key: 'forceRefenenceLength',
        showStatus: 'rePara',
        rules: [{ min: 0, type: 'number', message: '请输入大于0的数' }],
      },
      {
        label: '参考展长b(m)',
        key: 'forceRefenenceLengthSpanWise',
        options: ['-1.0', 0],
        type: 'Input',
        showStatus: 'rePara',
        rules: [{ min: 0, type: 'number', message: '请输入大于0的数' }],
      },
      {
        label: '参考面积(m²)',
        key: 'forceRefenenceArea',
        options: ['-1.0', 0],
        type: 'Input',
        showStatus: 'rePara',
        rules: [{ min: 0, type: 'number', message: '请输入大于0的数' }],
      },
      {
        label: '参考坐标点 X(m)',
        type: 'Input',
        key: 'forceRefenenceX',
        showStatus: 'rePara',
        rules: [],
      },
      {
        label: '参考坐标点 Y(m)',
        type: 'Input',
        key: 'forceRefenenceY',
        showStatus: 'rePara',
        rules: [],
      },
      {
        label: '参考坐标点 Y(m)',
        type: 'Input',
        key: 'forceRefenenceZ',
        showStatus: 'rePara',
        rules: [],
      },
      {
        label: '计算绞链力矩',
        options: [
          ['打开', 1],
          ['关闭', 0],
        ],
        type: 'CheckBox',
        key: 'dumpHingeMoment',
      },
      {
        showStatus: 'dumpHingeMoment',
        label: '起点坐标',
        options: [
          ['x', 0],
          ['y', 0],
          ['z', 0],
        ],
        type: 'GroupInput',
        key: 'localCoordAxis0',
      },
      {
        showStatus: 'dumpHingeMoment',
        label: '终点坐标',
        options: [
          ['x', 0],
          ['y', 0],
          ['z', 1],
        ],
        type: 'GroupInput',
        key: 'localCoordAxis1',
      },
    ],
  },
  {
    type: '对称面边界条件',
    key: 3,
  },
  {
    type: '远场-无量纲参数',
    key: 4,
    subkey: 0,
    params: [
      {
        label: '马赫数',
        type: 'MultiSelect',
        key: 'reference_mach_number',
        rules: [],
      },
      {
        label: '攻角(°)',
        key: 'attackd',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '侧滑角(°)',
        key: 'sideslipd',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '雷诺数(/m)',
        key: 'reynolds',
        type: 'Input',
        rules: [{ min: 0, type: 'number', message: '请输入大于0的数' }],
      },
      {
        label: '来流温度(K)',
        type: 'Input',
        key: 'reference_temperature_dimensional',
        rules: [{ min: 0, type: 'number', message: '请输入大于0的数' }],
      },
    ],
  },
  {
    type: '远场-飞行参数',
    key: 4,
    subkey: 1,
    params: [
      {
        label: '马赫数',
        key: 'reference_mach_number',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '攻角(°)',
        key: 'attackd',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '侧滑角(°)',
        type: 'MultiSelect',
        key: 'sideslipd',
        rules: [],
      },
      {
        label: '高度(Km)',
        type: 'MultiSelect',
        key: 'height',
        rules: [],
      },
    ],
  },
  {
    type: '远场-试验参数',
    key: 4,
    subkey: 2,
    params: [
      {
        label: '马赫数',
        key: 'reference_mach_number',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '攻角(°)',
        key: 'attackd',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '侧滑角(°)',
        key: 'sideslipd',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '总温',
        key: 'reference_temperature_dimensional',
        type: 'Input',
        rules: [],
      },
      {
        label: '总压（Pa）',
        key: 'reference_pressure_dimensional',
        type: 'Input',
        rules: [],
      },
    ],
  },
  {
    type: '入口-无量纲参数',
    key: 5,
    subkey: 0,
    params: [
      {
        label: '马赫数',
        key: 'reference_mach_number',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '攻角(°)',
        key: 'attackd',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '侧滑角(°)',
        key: 'sideslipd',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '雷诺数(/m)',
        key: 'reynolds',
        type: 'Input',
        rules: [],
      },
      {
        label: '来流温度(K)',
        key: 'reference_temperature_dimensional',
        type: 'Input',
        rules: [],
      },
    ],
  },
  {
    type: '入口-飞行参数',
    key: 5,
    subkey: 1,
    params: [
      {
        label: '马赫数',
        key: 'reference_mach_number',
        type: 'MultiSelect',
        rules: [],
      },
      {
        label: '攻角(°)',
        key: 'attackd',
        type: 'MultiSelect',
      },
      {
        label: '侧滑角(°)',
        key: 'sideslipd',
        type: 'MultiSelect',
      },
      {
        label: '高度(Km)',
        key: 'height',
        type: 'MultiSelect',
      },
    ],
  },
  {
    type: '出口边界条件',
    key: 6,
  },
  {
    type: '极性轴边界条件',
    key: 7,
  },
  {
    type: '压力入口边界条件',
    key: 52,
    params: [
      {
        label: '压力入口方向',
        options: [
          ['边界面向法', 2],
          ['自定义方向向量', 0],
        ],
        key: 'directionMethod',
        type: 'Select',
      },
      {
        label: '总压',
        key: 'totalP_inlet',
        type: 'Input',
        rules: [],
      },
      {
        label: '总温',
        key: 'totalT_inlet',
        type: 'Input',
        rules: [],
      },
      {
        label: '马赫数',
        key: 'reference_mach_number',
        type: 'Input',
        rules: [],
      },
      {
        label: '参考温度(K)',
        key: 'reference_temperature_dimensional',
        type: 'Input',
        rules: [],
      },
      {
        label: '参考压力(Pa)',
        key: 'reference_pressure_dimensional',
        type: 'Input',
        rules: [],
      },
      {
        label: '方向失量',
        options: [
          ['x', 0],
          ['y', 0],
          ['z', 0],
        ],
        type: 'GroupInput',
        key: 'localCoordAxis0',
      },
    ],
  },
  {
    type: '压力出口边界条件',
    key: 62,
    params: [
      {
        label: '总压',
        type: 'Input',
        key: 'totalP_inlet',
        rules: [],
      },
      {
        label: '总温',
        type: 'Input',
        key: 'totalT_inlet',
        rules: [],
      },
      {
        label: '马赫数',
        type: 'Input',
        key: 'reference_mach_number',
        rules: [],
      },
      {
        label: '参考温度(K)',
        type: 'Input',
        key: 'reference_temperature_dimensional',
        rules: [],
      },
      {
        label: '参考压力(Pa)',
        type: 'Input',
        key: 'reference_pressure_dimensional',
        rules: [],
      },
    ],
  },
]

const spatialDispersion: ParamProps[] = [
  {
    label: '空间离散格式',
    visible: false,
    options: ['roe', 'vanleer', 'steger', 'ausmpw', 'ausmpwplus'],
    type: ParamComponent.Select,
    key: 'str_scheme_name',
  },
  {
    label: '限制器',
    options: ['vanalbada', 'minvan', 'vanleer', 'minmod', 'nolim', 'smooth'],
    type: ParamComponent.Select,
    key: 'str_limiter_name',
  },
  {
    label: 'MUSCL插值精度',
    type: ParamComponent.Select,
    key: 'xkmuscl',
    defaultValue: '2阶迎风',
    options: [
      ['2阶迎风', -1.0],
      ['3阶偏置', 0.333333],
    ],
  },
  {
    label: '无粘项离散格式',
    options: [
      'vanleer',
      'roe',
      'steger',
      'kfvs',
      'lax_f',
      'hlle',
      'ausm+',
      'ausmdv',
      'ausm+w',
      'ausmpw',
      'ausmpwplus',
    ],
    type: ParamComponent.Select,
    key: 'uns_scheme_name',
  },
  {
    label: '限制器',
    options: ['barth', 'vencat', '1st', 'nolim'],
    type: ParamComponent.Select,
    key: 'uns_limiter_name',
  },
  {
    label: '粘性项计算方法',
    options: [
      ['标准型', 'std'],
      ['修正型', 'test'],
      ['平均型', 'aver'],
    ],
    type: ParamComponent.Select,
    key: 'uns_vis_name',
  },
  {
    label: '梯度计算方法',
    options: [
      ['ggcell', 'ggcell'],
      ['ggcellw', 'ggcellw'],
      ['ggnode', 'ggnode'],
      ['ggnode_weight', 'ggnode_weight'],
    ],
    type: ParamComponent.Select,
    key: 'uns_gradient_name',
  },
  {
    label: '限制变量',
    options: [
      ['全部变量限制', 1],
      ['仅密度压力限制', 0],
    ],
    type: ParamComponent.Select,
    key: 'limit_mode',
  },
  {
    label: '标量/矢量限制',
    options: [
      ['标量限制', 1],
      ['矢量限制', 0],
    ],
    type: ParamComponent.Select,
    key: 'limiter_vec',
  },
  {
    label: '熵修正缩放',
    type: ParamComponent.InputNumber,
    key: 'roeEntropyScale',
  },
  {
    label: 'Vencat限制器系数',
    type: ParamComponent.InputNumber,
    key: 'eps_vencat',
    rules: [
      { required: true, message: `请填写Vencat限制器系数` },
      { min: 0, type: 'number', message: '请输入大于0的数' },
      { max: 444, type: 'number', message: '请输入小于444的数' },
    ],
  },
]

const monitoringPanel: ParamProps[] = [
  {
    label: '类型',
    type: ParamComponent.Select,
    options: [
      ['POINTS', 0],
      ['GRID', 1],
      ['SURFACE', 2],
      ['OUTLINE', 3],
    ],
    key: 'show_type',
    box: 'set',
  },
  {
    label: '标量场',
    type: ParamComponent.Select,
    options: [
      ['density', 0],
      ['u', 1],
      ['v', 2],
      ['w', 3],
      ['pressure', 4],
      ['temperature', 5],
      ['mach', 6],
      // ['viscosityLaminar', 7],
      // ['viscosityTurbulent', 8],
      // ['vorticity', 9],
      // ['vorticityMagnitude', 10],
      ['cp', 15],
    ],
    key: 'cur_scalarIndex',
    box: 'set',
  },
  {
    type: ParamComponent.Radio,
    box: 'set',
    label: 'contour',
    options: [
      ['关闭', 0],
      ['打开', 1],
    ],
    key: 'contour_enable',
  },
  {
    type: ParamComponent.Radio,
    box: 'set',
    label: 'stream',
    options: [
      ['关闭', 0],
      ['打开', 1],
    ],
    key: 'stream_enable',
  },
  {
    box: 'scope',
    label: 'x',
    type: ParamComponent.Input,
    key: 'x_bound',
    visible: true,
  },
  {
    box: 'scope',
    label: 'y',
    type: ParamComponent.Input,
    key: 'y_bound',
    visible: true,
  },
  {
    box: 'scope',
    label: 'z',
    type: ParamComponent.Input,
    key: 'z_bound',
    visible: true,
  },
  // {
  //   label: '结束库朗数',
  //   type: ParamComponent.InputNumber,
  //   key: 'cfl_end',
  // },
  // {
  //   label: '变库朗数步数',
  //   type: ParamComponent.InputNumber,
  //   key: 'cfl_nstep',
  // },
  // {
  //   label: '低速预处理',
  //   options: [
  //     ['关闭', 0],
  //     ['打开', 1],
  //   ],
  //   type: ParamComponent.Radio,
  //   key: 'precon',
  // },
]

// const : ParamProps[] = [
//   {
//     label: '类型',
//     type: ParamComponent.Select,
//     options: [
//       ['POINTS', 0],
//       ['GRID', 1],
//       ['SURFACE', 2],
//       ['OUTLINE', 3],
//     ],
//     key: 'show_type',
//   },
//   {
//     label: '标量场',
//     type: ParamComponent.Select,
//     options: [
//       ['density', 0],
//       ['u', 1],
//       ['v', 2],
//       ['w', 3],
//       ['pressure', 4],
//       ['temperature', 5],
//       ['mach', 6],
//       ['viscosityLaminar', 7],
//       ['viscosityTurbulent', 8],
//       ['vorticity', 9],
//       ['vorticityMagnitude', 10],
//       ['cp', 15],
//     ],
//     key: 'cur_scalarIndex',
//   },
// ]
const timeDispersion: ParamProps[] = [
  {
    label: '多重网格',
    type: ParamComponent.Select,
    options: [
      ['1', 1],
      ['2', 2],
      ['3', 3],
      ['4', 4],
    ],
    key: 'mgrid',
  },
  {
    label: '起始库朗数',
    type: ParamComponent.InputNumber,
    key: 'cfl_start',
    box: 'courant',
    rules: [
      { required: true, message: `请填写起始库朗数` },
      { min: 0, type: 'number', message: '请输入大于0的数' },
    ],
  },
  {
    label: '结束库朗数',
    type: ParamComponent.InputNumber,
    key: 'cfl_end',
    box: 'courant',
    rules: [
      { required: true, message: `请填写结束库朗数` },
      { min: 0, type: 'number', message: '请输入大于0的数' },
    ],
  },
  {
    label: '变库朗数步数',
    type: ParamComponent.InputNumber,
    key: 'cfl_nstep',
    box: 'courant',
    rules: [
      { required: true, message: `请填写变库朗数步数` },
      {
        pattern: /^[0-9]+$/,
        message: '变库朗数步数必须是正整数',
      },
    ],
  },
  {
    label: '最小迭代步数',
    type: ParamComponent.InputNumber,
    key: 'min_sub_iter',
  },
  {
    label: '最大迭代步数',
    type: ParamComponent.InputNumber,
    key: 'max_sub_iter',
  },
  {
    label: '收敛判据',
    type: ParamComponent.InputNumber,
    key: 'tol_sub_iter',
  },
  {
    label: '前后扫描步数',
    type: ParamComponent.InputNumber,
    key: 'sweeps',
  },
  {
    label: '低速预处理',
    options: [
      ['关闭', 0],
      ['打开', 1],
    ],
    type: ParamComponent.Radio,
    key: 'precon',
  },
]

const postprocessing: ParamProps[] = [
  {
    label: '参考长度l(m)',
    type: ParamComponent.InputNumber,
    key: 'forceRefenenceLength',
    box: 'aerodynamic',
  },
  {
    label: '参考展长b(m)',
    type: ParamComponent.InputNumber,
    key: 'forceRefenenceLengthSpanWise',
    box: 'aerodynamic',
  },
  {
    label: '参考面积(m²)',
    type: ParamComponent.InputNumber,
    key: 'forceRefenenceArea',
    box: 'aerodynamic',
  },
  {
    label: '参考坐标点 X(m)',
    type: ParamComponent.InputNumber,
    key: 'forceRefenenceX',
    box: 'aerodynamic',
  },
  {
    label: '参考坐标点 Y(m)',
    type: ParamComponent.InputNumber,
    key: 'forceRefenenceY',
    box: 'aerodynamic',
  },
  {
    label: '参考坐标点 Z(m)',
    type: ParamComponent.InputNumber,
    key: 'forceRefenenceZ',
    box: 'aerodynamic',
  },
  {
    label: '残差输出间隔',
    type: ParamComponent.InputNumber,
    key: 'nressave',
    box: 'outputsteps',
  },
  {
    label: '气动力输出间隔',
    type: ParamComponent.InputNumber,
    key: 'nforcsave',
    box: 'outputsteps',
  },
  {
    label: '流场显示输出间隔',
    type: ParamComponent.InputNumber,
    key: 'nplotsave',
    box: 'outputsteps',
  },
  {
    label: '流场数据输出间隔',
    type: ParamComponent.InputNumber,
    key: 'ndisk',
    box: 'outputsteps',
  },
]

const calcResult: ParamProps[] = [
  {
    label: '是否导出流场结果',
    type: ParamComponent.Radio,
    options: [
      ['不输出', 0],
      ['输出', 1],
    ],
    key: 'visual_field',
    box: 'result',
  },
  {
    label: '计算残差',
    type: ParamComponent.Input,
    key: 'resfile',
    visible: true,
    box: 'result',
  },
  {
    label: '湍流残差',
    type: ParamComponent.Input,
    key: 'turbresfile',
    visible: true,
    box: 'result',
  },
  {
    label: '气动力系数',
    type: ParamComponent.Input,
    key: 'aircoeffile',
    visible: true,
    box: 'result',
  },
  {
    label: '流场变量',
    type: ParamComponent.Input,
    key: 'flowfile',
    visible: true,
    box: 'result',
  },
  {
    label: '湍流变量',
    type: ParamComponent.Input,
    key: 'turbfile',
    visible: true,
    box: 'result',
  },
  {
    label: '流场显示',
    visible: true,
    type: ParamComponent.Input,
    key: 'visualfile',
    box: 'result',
  },
  {
    label: '壁面数据',
    type: ParamComponent.Input,
    visible: true,
    key: 'wall_aircoefile',
    box: 'result',
  },
  {
    label: '流场参数输出编号',
    visible: true,
    options: [
      ['density', 0],
      ['u', 1],
      ['v', 2],
      ['w', 3],
      ['pressure', 4],
      ['temperature', 5],
      ['mach', 6],
      ['viscosityLaminar', 7],
      ['viscosityTurbulent', 8],
      ['vorticity_x', 9],
      ['vorticity_y', 10],
      ['vorticity_z', 11],
      ['vorticityMagnitude', 12],
      ['strain_rate', 13],
      ['Q_criteria', 14],
      ['Cp', 15],
      ['timeStep', 16],
      ['volume', 17],
    ],
    type: ParamComponent.MultiSelect,
    key: 'visualVariables',
    box: 'result',
  },
]

export const sections = [
  {
    name: '控制参数',
    params: turbulenceParams,
    type: SettingComponent.Turbulence,
    description:
      '非定常数值模拟若是从定常流场续算，请到高级模式中勾选“定常流场续算”。',
  },
  {
    name: '空间离散',
    params: spatialDispersion,
    type: SettingComponent.SpaceBar,
    description:
      'vencat选项，系数范围0.1～50，数值越小耗散越大。马赫数越高，应采用较小值；反之亦然。',
  },
  {
    name: '时间离散',
    params: timeDispersion,
    type: SettingComponent.Common,
    description: '无量纲时间步长推荐采用0.01。',
  },
  {
    name: '后置处理',
    params: postprocessing,
    type: SettingComponent.Common,
    description: '后置处理参数仅对后处理输出部分有效。',
  },
  {
    name: '计算结果',
    params: calcResult,
    type: SettingComponent.Common,
    description: '文件存储位置在工作目录下',
  },
]

export const sectionsRight = [
  {
    name: '菜单',
    icon: 'menu',
    params: monitoringPanel,
    type: SettingComponent.Common,
  },
  // {
  //   name: '放大',
  //   icon: 'amplification',
  //   params: timeDispersion,
  //   type: SettingComponent.Common,
  // },
  // {
  //   name: '缩小',
  //   icon: 'reduce',
  //   params: postprocessing,
  //   type: SettingComponent.Common,
  // },
  {
    name: '刷新',
    icon: 'cycle',
    params: monitoringPanel,
    type: SettingComponent.Common,
  },
]

const PIEchartConfig = {
  height: 280,
  radius: 0.8,
  angleField: 'data',
  colorField: 'type',
  label: {
    visible: true,
    type: 'outer',
    offset: 20,
    formatter: angleField => {
      return `${angleField.data.toFixed(2)}%`
    },
  },
  legend: {
    visible: true,
    position: 'top-left',
    formatter: type => {
      return {
        use: '已使用',
        free: '未使用',
      }[type]
    },
  },
  tooltip: {
    visible: true,
    fields: ['data', 'type'],
    formatter: e => {
      return {
        name: {
          use: '已使用',
          free: '未使用',
        }[e.type],
        value: `${e.data.toFixed(2)}%`,
      }
    },
  },
}

interface ChartProps {
  name: string
  chartType: string
  chartConfig: any
  title?: string
  isNodeData?: boolean
  data?: any[]
}

export const Report: ChartProps[] = [
  {
    name: 'MEMORY',
    chartType: 'LINE',
    chartConfig: {
      type: 'Report',
    },
    title: '内存容量',
  },
  {
    name: 'DISK',
    chartType: 'LINE',
    chartConfig: {
      type: 'Report',
    },
    title: '磁盘空间',
  },
  {
    name: 'CPU',
    chartType: 'LINE',
    title: 'CPU使用率',
    chartConfig: {
      type: 'Report',
    },
  },
  {
    name: 'LOAD',
    chartType: 'LINE',
    title: '负载',
    chartConfig: {
      type: 'Report',
    },
  },
  {
    name: 'DISKIO',
    chartType: 'LINE',
    title: '磁盘读写',
    chartConfig: {
      type: 'Report',
    },
  },
  {
    name: 'NETWORK',
    chartType: 'LINE',
    title: '网络',
    chartConfig: {
      type: 'Report',
    },
  },
]
export const Monitor: ChartProps[] = [
  {
    name: 'MEMORY',
    chartType: 'PIE',
    chartConfig: PIEchartConfig,
    title: '内存容量',
  },
  {
    name: 'DISK',
    chartType: 'PIE',
    chartConfig: PIEchartConfig,
    title: '磁盘空间',
  },
  {
    name: 'CPU',
    chartType: 'LINE',
    title: 'CPU使用率',
    chartConfig: {
      type: 'Monitor',
    },
  },
  {
    name: 'LOAD',
    chartType: 'LINE',
    title: '负载',
    chartConfig: {
      type: 'Monitor',
    },
  },
  {
    name: 'DISKIO',
    chartType: 'LINE',
    title: '磁盘读写',
    chartConfig: {
      type: 'Monitor',
    },
  },
  {
    name: 'NETWORK',
    chartType: 'LINE',
    title: '网络',
    chartConfig: {
      type: 'Monitor',
    },
  },
  {
    name: 'one',
    chartType: 'COLUMN',
    title: '一分钟负载',
    chartConfig: {
      Yalias: '一分钟负载',
      type: 'Monitor',
    },
  },
  {
    name: 'five',
    chartType: 'COLUMN',
    title: '五分钟负载',
    chartConfig: {
      Yalias: '五分钟负载',
      type: 'Monitor',
    },
  },
  {
    name: 'fifteen',
    chartType: 'COLUMN',
    title: '十五分钟负载',
    chartConfig: {
      Yalias: '十五分钟负载',
      type: 'Monitor',
    },
  },
  {
    name: 'number',
    chartType: 'STACKEDCOLUMN',
    title: '内存使用量',
    chartConfig: {
      Yalias: '',
      type: 'Monitor',
    },
  },
  {
    name: 'percent',
    chartType: 'STACKEDCOLUMN',
    title: '内存使用比例',
    chartConfig: {
      Yalias: '%',
      type: 'Monitor',
    },
  },
  {
    name: 'cpu_node_datas',
    chartType: 'STACKEDCOLUMN',
    title: 'CPU详情',
    chartConfig: {
      Yalias: '%',
      type: 'Monitor',
    },
  },
  {
    name: 'disk_io_node_datas',
    chartType: 'GROUPEDCOLUMN',
    title: 'IO详情',
    chartConfig: {
      type: 'Monitor',
    },
  },
  {
    name: '/',
    chartType: 'GROUPEDCOLUMN',
    title: '根磁盘详情',
    chartConfig: {
      Yalias: 'KB/s',
      type: 'Monitor',
    },
  },
  {
    name: '/boot',
    chartType: 'GROUPEDCOLUMN',
    title: 'boot磁盘详情',
    chartConfig: {
      Yalias: 'KB/s',
      type: 'Monitor',
    },
  },
  {
    name: 'total',
    chartType: 'GROUPEDCOLUMN',
    title: 'total磁盘详情',
    chartConfig: {
      Yalias: 'KB/s',
      type: 'Monitor',
    },
  },
  {
    name: 'network_node_data',
    chartType: 'GROUPEDCOLUMN',
    title: '网速详情',
    chartConfig: {
      type: 'Monitor',
    },
  },
]


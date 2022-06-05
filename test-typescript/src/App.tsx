import React from 'react';
import { Form, Input, Button, Space } from 'antd';
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons';
import {onFinish} from './tmp'
import type { FormInstance } from 'antd/es/form';

// let res

// const onFinish = (values :any) => {
//   console.log('Received values of form:', values);
//   res = values;
//   console.log(res)
//   return values;
// };



const App: React.FC = () => {

  formRef = React.createRef<FormInstance>();
  return (
    <Form name="dynamic_form_nest_item" ref={formRef} onFinish={onFinish} autoComplete="off">
      <Form.List name="users">
        {(fields, { add, remove }) => (
          <>
            {fields.map(({ key, name, ...restField }) => (
              <Space
                key={key}
                style={{
                  display: 'flex',
                  marginBottom: 8,
                }}
                align="baseline"
              >
                <Form.Item
                  {...restField}
                  name={[name, 'paramname']}
                  rules={[
                    {
                      required: true,
                      message: 'Missing param name',
                    },
                  ]}
                >
                  <Input placeholder="Param Name" />
                </Form.Item>
                <Form.Item
                  {...restField}
                  name={[name, 'type']}
                  rules={[
                    {
                      required: true,
                      message: 'Missing Var Type',
                    },
                  ]}
                >
                  <Input placeholder="Var Type" />
                </Form.Item>
                <Form.Item
                  {...restField}
                  name={[name, 'name']}
                  rules={[
                    {
                      required: true,
                      message: 'Missing Var Name',
                    },
                  ]}
                >
                  <Input placeholder="Var Name" />
                </Form.Item>
                <Form.Item
                  {...restField}
                  name={[name, 'value']}
                  rules={[
                    {
                      required: true,
                      message: 'Missing Var Value ',
                    },
                  ]}
                >
                  <Input placeholder="Var Value" />
                </Form.Item>
                <MinusCircleOutlined onClick={() => remove(name)} />
              </Space>
            ))}
            <Form.Item>
              <Button type="dashed" onClick={() => add()} block icon={<PlusOutlined />}>
                Add field
              </Button>
            </Form.Item>
          </>
        )}
      </Form.List>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default App;

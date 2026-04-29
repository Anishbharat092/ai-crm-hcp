import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  hcpName: '',
  date: '',
  time: '',
  type: '',
  topics: '',
  sentiment: '',
  outcomes: '',
  followUps: ''
};

const interactionSlice = createSlice({
  name: 'interaction',
  initialState,
  reducers: {
    updateField: (state, action) => {
      state[action.payload.field] = action.payload.value;
    },
    setAll: (state, action) => {
      return { ...state, ...action.payload };
    }
  }
});

export const { updateField, setAll } = interactionSlice.actions;
export default interactionSlice.reducer;
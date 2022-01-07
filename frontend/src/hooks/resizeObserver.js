import { ref, reactive, onMounted, onBeforeUnmount } from "vue";

export const useResizeObserver = () => {
  const resizeRef = ref();
  const resizeState = reactive({
    dimensions: {}
  });

  const observer = new ResizeObserver(entries => {
    entries.forEach(entry => {
      resizeState.dimensions = entry.contentRect;
    });
  });

  onMounted(() => {
    // set initial dimensions right before observing: Element.getBoundingClientRect()
    resizeState.dimensions = resizeRef.value.getBoundingClientRect();
    observer.observe(resizeRef.value);
  });

  onBeforeUnmount(() => {
    observer.unobserve(resizeRef.value);
  });

  return { resizeState, resizeRef };
};

export default useResizeObserver;